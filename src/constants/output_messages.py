
class OutputMessages:
    INVALID_CHOICE = None
    USER_CREATED = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.INVALID_CHOICE = json_data["invalid_choice"]
        cls.USER_CREATED = json_data["user_created"]

