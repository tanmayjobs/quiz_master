
class InputTexts:
    USERNAME = None
    PASSWORD = None
    USER_ID = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME = data["username"]
        cls.PASSWORD = data["password"]
        cls.USER_ID = data["user_id"]
