
class OutputTexts:
    INVALID_CHOICE = None
    USER_ADDED = None
    CREATOR_ADDED = None

    @classmethod
    def __init__(cls, data):
        cls.INVALID_CHOICE = data["invalid_choice"]
        cls.USER_ADDED = data["user_added"]
        cls.CREATOR_ADDED = data["creator_added"]
