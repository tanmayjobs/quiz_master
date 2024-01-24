import uuid

from pymysql import IntegrityError

from data_containers.user import User
from database import MysqlAccess, database, DatabaseAccess
from helpers.constants import SQLQueries
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import DBException, InvalidCredentials, AlreadyExists
from utils.crypt import check_password, hash_password


class AuthServices:
    def __init__(self, database_access=None):
        self.database_access: DatabaseAccess = database_access or MysqlAccess(database)

    def sign_in(self, username, password):
        with self.database_access as dao:
            user_data = dao.read(SQLQueries.GET_USER, (username,), True)

        if not user_data or not check_password(password, user_data["hash_password"]):
            raise InvalidCredentials(HTTPStatuses.UNAUTHORIZED.code, HTTPStatuses.UNAUTHORIZED.status, "username and password do not match!")

        user = User(**user_data)
        return user

    def sign_up(self, username, password):
        password_hash = hash_password(password)
        try:
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_USER, (uuid.uuid4(), username, password_hash, UserRole.PLAYER.value),)
        except IntegrityError:
            raise AlreadyExists(HTTPStatuses.CONFLICT.code, HTTPStatuses.CONFLICT.status, "username already exists!")
