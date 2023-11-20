class Strings:
    ADMIN = None
    CREATOR = None
    PLAYER = None
    QUIZ = None
    ID = None
    USER = None
    USERNAME = None
    ROLE = None
    QUESTION = None
    OPTION = None
    TYPE = None
    RESULT = None
    A = None
    QUIZ_NAME = None
    ALL_QUESTIONS = None

    MOVIE = None
    MUSIC = None
    BOOK = None
    OTHER = None

    PERFORMER = None

    OPTIONS_JSON = None
    QUESTION_TEXT = None
    QUESTION_ID = None
    IS_CORRECT = None

    ARRAY = None
    FILTER = None

    TYPE_ID = None
    TYPE_NAME = None

    PLAYED_AT = None
    RESULT_PERCENTAGE = None

    PASSWORD_REGEX = None

    @classmethod
    def __init__(cls, data):
        cls.ADMIN = data["admin"]
        cls.CREATOR = data["creator"]
        cls.PLAYER = data["player"]
        cls.QUIZ = data["quiz"]
        cls.ID = data["id"]
        cls.USER = data["user"]
        cls.USERNAME = data["username"]
        cls.ROLE = data["role"]
        cls.QUESTION = data["question"]
        cls.OPTION = data["option"]
        cls.TYPE = data["type"]
        cls.RESULT = data["result"]
        cls.A = data["a"]
        cls.QUIZ_NAME = data["quiz_name"]
        cls.ALL_QUESTIONS = data["all_questions"]

        cls.MOVIE = data["movie"]
        cls.MUSIC = data["music"]
        cls.BOOK = data["book"]
        cls.OTHER = data["other"]

        cls.PERFORMER = data["performer"]

        cls.OPTIONS_JSON = data["options_json"]
        cls.QUESTION_TEXT = data["question_text"]
        cls.QUESTION_ID = data["question_id"]
        cls.IS_CORRECT = data["is_correct"]

        cls.ARRAY = data["array"]
        cls.FILTER = data["filter"]

        cls.TYPE_ID = data["type_id"]
        cls.TYPE_NAME = data["type_name"]

        cls.PLAYED_AT = data["played_at"]
        cls.RESULT_PERCENTAGE = data["result_percentage"]

        cls.PASSWORD_REGEX = data["password_regex"]
