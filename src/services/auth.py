import uuid

from pymysql import IntegrityError

from database import MysqlAccess, DatabaseAccess, SqliteAccess
from helpers.constants import SQLQueries, Strings, Errors, LogText
from helpers.enum.user_role import UserRole
from helpers.exceptions import InvalidCredentials, AlreadyExists, DoNotExists
from helpers.log import request_logger
from utils.hashing import check_password, hash_password


class AuthServices:
    def __init__(self, database_access=None):
        self.database_access: DatabaseAccess = database_access or SqliteAccess()

    def sign_in(self, username, password):
        with self.database_access as dao:
            user_data = dao.read(SQLQueries.GET_USER, (username,), True)

        if not user_data:
            raise DoNotExists("")
        if not check_password(
            password, user_data[Strings.HASH_PASSWORD]
        ):
            raise InvalidCredentials(Errors.INVALID_CREDENTIALS)
        return user_data

    def sign_up(self, username, password):
        password_hash = hash_password(password)
        try:
            with self.database_access as dao:
                dao.write(
                    SQLQueries.ADD_USER,
                    (uuid.uuid4(), username, password_hash, UserRole.PLAYER.value),
                )
        except IntegrityError as error:
            request_logger.info(error)
            raise AlreadyExists(Errors.USERNAME_ALREADY_EXISTS.format(username))
