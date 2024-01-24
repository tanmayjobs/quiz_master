from sqlite3 import IntegrityError

from data_containers.user import *
from database import database, DBContext
from helpers.constants import SQLQueries
from utils.crypt import check_password, hash_password

import uuid


class AuthHandler:
    """
    This handler is used for authentication process.
    It takes username and password as parameters and provide sign in and sign up functionality.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self) -> User | None:
        if not self.username.strip() or not self.password:
            return None

        with DBContext(database) as dao:
            user_data = dao.read(SQLQueries.GET_USER, (self.username,), True)

        if not user_data:
            return None

        user = User(**user_data)
        if not check_password(self.password, user.password_hash):
            return None

        return user

    def sign_up(self) -> bool:
        if not self.username.strip() or not self.password:
            return False
        password_hash = hash_password(self.password)

        try:
            with DBContext(database) as dao:
                is_user_added = (
                    dao.write(
                        SQLQueries.ADD_USER,
                        (uuid.uuid4(), self.username, password_hash, UserRole.PLAYER.value),
                    ).rows_changed
                    > 0
                )
        except IntegrityError:
            is_user_added = False

        return is_user_added
