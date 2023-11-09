class ERROR:
    USERNAME_ALREADY_EXISTS = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.USERNAME_ALREADY_EXISTS = json["username_already_exists"]

