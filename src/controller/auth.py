from sqlite3 import IntegrityError

from helpers.constants import SQLQueries
from data_containers.user import *
from database import database
from utils.crypt import check_password, hash_password


class AuthHandler:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self) -> User | None:
        if not self.username.strip() or not self.password:
            return None

        user_data = database.get(SQLQueries.GET_USER, (self.username,), True)
        if not user_data:
            return None

        user = User.parse_database(user_data)
        if not check_password(self.password, user.password_hash):
            return None

        return user

    def sign_up(self) -> bool:
        if not self.username.strip() or not self.password:
            return False
        password_hash = hash_password(self.password)

        try:
            is_user_added = database.add(SQLQueries.ADD_USER, (self.username, password_hash, UserRole.PLAYER))
        except IntegrityError:
            is_user_added = False

        return is_user_added
