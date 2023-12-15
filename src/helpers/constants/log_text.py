class LogText:
    SYSTEM_START = None
    SYSTEM_EXIT = None
    SYSTEM_ERROR = None
    INVALID_CREDENTIALS = None
    READING_DATA = None
    WRITING_DATA = None

    @classmethod
    def __init__(cls, data):
        cls.SYSTEM_START = data["system_start"]
        cls.SYSTEM_EXIT = data["system_exit"]
        cls.SYSTEM_ERROR = data["system_error"]
        cls.INVALID_CREDENTIALS = data["invalid_credentials"]
        cls.READING_DATA = data["reading_data"]
        cls.WRITING_DATA = data["writing_data"]
