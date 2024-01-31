import uuid

from flask_jwt_extended import create_access_token, create_refresh_token

from database import DatabaseAccess, SqliteAccess, token_database
from helpers.constants import LogText, SQLQueries, Strings
from helpers.log import logger


class TokenService:
    blocked_token_pair_ids = set()
    blocked_tokens = set()

    def __init__(self, database_access=None):
        self.database_access: DatabaseAccess = database_access or SqliteAccess(token_database)

    def invalidate_token_pair(self, token_pair_id, user_id, exp):
        self.blocked_tokens.add((token_pair_id, user_id, exp))
        self.blocked_token_pair_ids.add(token_pair_id)

    def refresh_access_token(self, user_id, jwt):
        user = {
            Strings.ID: user_id,
            Strings.USER_ROLE: jwt[Strings.ROLE]
        }
        self.invalidate_token_pair(jwt[Strings.TOKEN_PAIR_ID], user_id, jwt[Strings.EXP])
        return self.generate_tokens(user, fresh=False)

    def generate_tokens(self, user, fresh=False):
        token_pair_id = uuid.uuid4()
        return {
            Strings.ACCESS_TOKEN: create_access_token(
                identity=user[Strings.ID],
                additional_claims={
                    Strings.ROLE: user[Strings.USER_ROLE],
                    Strings.TOKEN_PAIR_ID: token_pair_id
                },
                fresh=fresh
            ),
            Strings.REFRESH_TOKEN: create_refresh_token(
                identity=user[Strings.ID],
                additional_claims={
                    Strings.ROLE: user[Strings.USER_ROLE],
                    Strings.TOKEN_PAIR_ID: token_pair_id
                }
            )
        }

    @classmethod
    def load_tokens(cls):
        logger.info(LogText.LOADING_TOKEN)
        with SqliteAccess(token_database) as dao:
            tokens = dao.read(SQLQueries.LOAD_TOKEN)
        cls.blocked_token_pair_ids.update(tuple(map(lambda token: token[0], tokens)))
        cls.blocked_tokens.update(tokens)

    @classmethod
    def save_tokens(cls):
        logger.info(LogText.SAVING_TOKEN)
        with SqliteAccess(token_database) as dao:
            dao.write_many(SQLQueries.SAVE_TOKEN, *cls.blocked_tokens)
