
class OutputTexts:
    INVALID_CHOICE = None
    USER_CREATED = None

    @classmethod
    def __init__(cls, data):
        cls.INVALID_CHOICE = data["invalid_choice"]
        cls.USER_CREATED = data["user_created"]

