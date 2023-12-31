class Errors:
    WEAK_PASSWORD = None
    USERNAME_EMPTY = None
    PASSWORD_EMPTY = None
    USERNAME_ALREADY_EXISTS = None
    INVALID_CREDENTIALS = None
    INVALID_INPUT = None
    PERMISSION = None
    PERFORMER_REQUIRED = None
    UNEXPECTED_ERROR = None

    @classmethod
    def __init__(cls, data):
        cls.WEAK_PASSWORD = data["weak_password"]
        cls.USERNAME_EMPTY = data["username_empty"]
        cls.PASSWORD_EMPTY = data["password_empty"]
        cls.USERNAME_ALREADY_EXISTS = data["username_already_exists"]
        cls.INVALID_CREDENTIALS = data["invalid_credentials"]
        cls.INVALID_INPUT = data["invalid_input"]
        cls.PERMISSION = data["permission"]
        cls.PERFORMER_REQUIRED = data["performer_required"]
        cls.UNEXPECTED_ERROR = data["unexpected_error"]
