class Errors:
    USERNAME_ALREADY_EXISTS = None
    INVALID_CREDENTIALS = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME_ALREADY_EXISTS = data["username_already_exists"]
        cls.INVALID_CREDENTIALS = data["invalid_credentials"]

