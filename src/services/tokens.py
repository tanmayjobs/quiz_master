import uuid

from flask_jwt_extended import create_access_token, create_refresh_token

from database import DatabaseAccess, MysqlAccess
from helpers.constants import SQLQueries, Strings


class TokenService:
    blocked_tokens = set()

    def __init__(self, database_access=None):
        self.database_access: DatabaseAccess = database_access or MysqlAccess()

    def is_blocked(self, token_pair_id):
        with self.database_access as dao:
            token = dao.read(SQLQueries.LOAD_TOKEN, (token_pair_id,), only_one=True)
        return token is not None

    def invalidate_token_pair(self, token_pair_id, user_id, exp):
        with self.database_access as dao:
            dao.write(SQLQueries.SAVE_TOKEN, (token_pair_id, user_id, exp))

    def refresh_access_token(self, user_id, jwt):
        user = {Strings.ID: user_id, Strings.USER_ROLE: jwt[Strings.ROLE]}
        self.invalidate_token_pair(
            jwt[Strings.TOKEN_PAIR_ID], user_id, jwt[Strings.EXP]
        )
        return self.generate_tokens(user, fresh=False)

    @classmethod
    def generate_tokens(cls, user, fresh=False):
        token_pair_id = uuid.uuid4()
        return {
            Strings.ACCESS_TOKEN: create_access_token(
                identity=user[Strings.ID],
                additional_claims={
                    Strings.ROLE: user[Strings.USER_ROLE],
                    Strings.TOKEN_PAIR_ID: token_pair_id,
                },
                fresh=fresh,
            ),
            Strings.REFRESH_TOKEN: create_refresh_token(
                identity=user[Strings.ID],
                additional_claims={
                    Strings.ROLE: user[Strings.USER_ROLE],
                    Strings.TOKEN_PAIR_ID: token_pair_id,
                },
            ),
        }
