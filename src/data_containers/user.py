from helpers.enums import UserRole


class User:

    def __init__(self, user_id: int, username: str, password_hash: str,
                 role: UserRole):
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

    @staticmethod
    def parse_database(row):
        user_id, username, password_hash, role = row[:4]
        return User(user_id, username, password_hash, role)

    def __repr__(self):
        return f"{self.username}, {self.role}"
