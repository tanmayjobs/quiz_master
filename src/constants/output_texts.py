
class OutputTexts:
    INVALID_CHOICE = None
    USER_ADDED = None
    QUIZ_ADDED = None
    CREATOR_ADDED = None
    USER_INFO = None
    TYPE_INFO = None
    QUIZ_INFO = None
    USER_REMOVED = None
    QUIZ_REMOVED = None
    ZERO_QUIZZES = None

    @classmethod
    def __init__(cls, data):
        cls.INVALID_CHOICE = data["invalid_choice"]
        cls.USER_ADDED = data["user_added"]
        cls.QUIZ_ADDED = data["quiz_added"]
        cls.CREATOR_ADDED = data["creator_added"]
        cls.USER_INFO = data["user_info"]
        cls.TYPE_INFO = data["type_info"]
        cls.QUIZ_INFO = data["quiz_info"]
        cls.USER_REMOVED = data["user_removed"]
        cls.QUIZ_REMOVED = data["quiz_removed"]
        cls.ZERO_QUIZZES = data["zero_quizzes"]
