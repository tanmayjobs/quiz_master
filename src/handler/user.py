from helpers.constants import SQLQueries
from database import database, DBContext
from utils.crypt import hash_password

from utils.rbac import accessed_by
from data_containers.user import *


class UserHandler:
    """
    This handler deals with users and requires a user.
    This handler is generally used by admin to create, remove and list users.
    """

    def __init__(self, user):
        self.user = user  # User who is trying to perform the operation

    @accessed_by(UserRole.ADMIN)
    def add_user(self,
                 username,
                 password,
                 role: UserRole = UserRole.CREATOR) -> bool:

        password_hash = hash_password(password)
        with DBContext(database) as dao:
            is_user_added = dao.write(SQLQueries.ADD_USER,
                                      (username, password_hash, role))

        return is_user_added

    @accessed_by(UserRole.ADMIN)
    def get_all_users(self) -> list[User]:
        with DBContext(database) as dao:
            all_user_data = dao.read(SQLQueries.GET_ALL_USERS)

        all_users = [
            User.parse_database(user_data) for user_data in all_user_data
        ]

        return all_users

    @accessed_by(UserRole.ADMIN)
    def remove_user(self, user_id) -> None:
        with DBContext(database) as dao:
            dao.write(SQLQueries.REMOVE_USER, (user_id,))
