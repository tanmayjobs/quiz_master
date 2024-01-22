from helpers.enum.user_role import UserRole


class User:
    def __init__(self, id: int, username: str, hash_password: str, user_role: UserRole):
        self.__user_id = id
        self.username = username
        self.__password_hash = hash_password
        self.role = user_role

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def password_hash(self):
        return self.__password_hash
