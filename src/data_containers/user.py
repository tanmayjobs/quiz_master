from helpers.enum.user_role import UserRole


class User:
    def __init__(self, id: int, username: str, user_role: UserRole, **_):
        self.__user_id = id
        self.username = username
        self.role = user_role

    @property
    def user_id(self) -> int:
        return self.__user_id
