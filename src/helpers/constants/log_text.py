class LogText:
    SYSTEM_START = None
    SYSTEM_EXIT = None
    SYSTEM_ERROR = None
    INVALID_CREDENTIALS = None

    @classmethod
    def __init__(cls, data):
        cls.SYSTEM_START = data["system_start"]
        cls.SYSTEM_EXIT = data["system_exit"]
        cls.SYSTEM_ERROR = data["system_error"]
        cls.INVALID_CREDENTIALS = data["invalid_credentials"]
