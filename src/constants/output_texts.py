
class OutputTexts:
    INVALID_CHOICE = None
    USER_ADDED = None
    QUIZ_ADDED = None
    CREATOR_ADDED = None
    QUESTION_ADDED = None
    USER_INFO = None
    TYPE_INFO = None
    QUIZ_INFO = None
    QUESTION_INFO = None
    RECORD_INFO = None
    USER_REMOVED = None
    QUIZ_REMOVED = None
    QUESTION_REMOVED = None
    ZERO_QUIZZES = None
    NOT_YET = None
    SIGN_OUT = None
    QUIZ_RESULT = None
    NO_QUIZ_RECORDS = None

    @classmethod
    def __init__(cls, data):
        cls.INVALID_CHOICE = data["invalid_choice"]
        cls.USER_ADDED = data["user_added"]
        cls.QUIZ_ADDED = data["quiz_added"]
        cls.CREATOR_ADDED = data["creator_added"]
        cls.QUESTION_ADDED = data["question_added"]
        cls.USER_INFO = data["user_info"]
        cls.TYPE_INFO = data["type_info"]
        cls.QUIZ_INFO = data["quiz_info"]
        cls.QUESTION_INFO = data["question_info"]
        cls.RECORD_INFO = data["record_info"]
        cls.USER_REMOVED = data["user_removed"]
        cls.QUIZ_REMOVED = data["quiz_removed"]
        cls.QUESTION_REMOVED = data["question_removed"]
        cls.ZERO_QUIZZES = data["zero_quizzes"]
        cls.NOT_YET = data["not_yet"]
        cls.SIGN_OUT = data["sign_out"]
        cls.QUIZ_RESULT = data["quiz_result"]
        cls.NO_QUIZ_RECORDS = data["no_quiz_records"]
