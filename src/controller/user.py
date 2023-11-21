from helpers.constants import SQLQueries
from database import database
from utils.crypt import hash_password

from utils.rbac import accessed_by
from data_containers.user import *


class UserHandler:

    def __init__(self, user):
        self.user = user    # User who is trying to perform the operation

    @accessed_by(UserRole.ADMIN)
    def add_user(self, username, password, role: UserRole = UserRole.CREATOR) -> bool:

        password_hash = hash_password(password)
        is_user_added = database.add(SQLQueries.ADD_USER, (username, password_hash, role))

        return is_user_added

    @accessed_by(UserRole.ADMIN)
    def get_all_users(self) -> list[User]:
        all_user_data = database.get(SQLQueries.GET_ALL_USERS)
        all_users = [User.parse_database(user_data) for user_data in all_user_data]

        return all_users

    @accessed_by(UserRole.ADMIN)
    def remove_user(self, user) -> None:
        database.remove(SQLQueries.REMOVE_USER, (user.user_id,))
