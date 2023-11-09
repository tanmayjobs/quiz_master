from enum import Enum


class UserRole(Enum):
    ADMIN = 0
    CREATOR = 1
    PLAYER = 2


class User:
    def __init__(self, user_id: int, username: str, password_hash: str, role: UserRole):
        self.__user_id = user_id
        self.username = username
        self.__password_hash = password_hash
        self.role = role

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def password_hash(self):
        return self.__password_hash
