from enum import Enum


class UserRole(Enum):
    ADMIN = 0
    CREATOR = 1
    PLAYER = 2


class User:
    def __init__(self, user_id: int, username: str, password_hash: str, role: UserRole):
        self.user_id = user_id
        self.username = username
        self.__password_hash = password_hash
        self.role = role

    @staticmethod
    def get(self):
        ...

    @staticmethod
    def add(self):
        ...

    @staticmethod
    def remove(self):
        ...


class Creator(User):
    def __init__(self, user_id: int, username: str, password_hash: str, role: UserRole, quizzes):
        super().__init__(user_id, username, password_hash, role)
        self.quizzes = quizzes
