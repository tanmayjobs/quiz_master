class Strings:
    ADMIN = None
    CREATOR = None
    PLAYER = None
    USER_ID = None
    USERNAME = None
    ROLE = None

    @classmethod
    def __init__(cls, data):
        cls.ADMIN = data["admin"]
        cls.CREATOR = data["creator"]
        cls.PLAYER = data["player"]
        cls.USER_ID = data["user_id"]
        cls.USERNAME = data["username"]
        cls.ROLE = data["role"]
