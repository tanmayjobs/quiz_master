class Config:
    SQL_FILE_PATH = None
    SQL_FILE_NAME = None
    SQL_DB_PATH = None

    LOGS_FILE_PATH = None
    LOG_FILEMODE = None
    LOG_FORMAT = None
    LOG_DATEFMT = None

    @classmethod
    def __init__(cls, data):
        cls.SQL_FILE_PATH = data["sql"]["file_path"]
        cls.SQL_FILE_NAME = data["sql"]["file_name"]
        cls.SQL_DB_PATH = data["sql"]["db_path"]

        cls.LOGS_FILE_PATH = data["logs"]["file_path"]
        cls.LOG_FILEMODE = data["logs"]["filemode"]
        cls.LOG_FORMAT = data["logs"]["format"]
        cls.LOG_DATEFMT = data["logs"]["datefmt"]
