class Strings:
    ADMIN = None
    CREATOR = None
    PLAYER = None
    QUIZ = None
    ID = None
    USERNAME = None
    ROLE = None
    QUESTION = None
    OPTION = None
    TYPE = None
    A = None
    QUIZ_NAME = None
    ALL_QUESTIONS = None

    MOVIE = None
    MUSIC = None
    BOOK = None

    PERFORMER = None

    OPTIONS_JSON = None
    QUESTION_TEXT = None
    QUESTION_ID = None
    IS_CORRECT = None

    ARRAY = None

    TYPE_ID = None
    TYPE_NAME = None

    @classmethod
    def __init__(cls, data):
        cls.ADMIN = data["admin"]
        cls.CREATOR = data["creator"]
        cls.PLAYER = data["player"]
        cls.QUIZ = data["quiz"]
        cls.ID = data["id"]
        cls.USERNAME = data["username"]
        cls.ROLE = data["role"]
        cls.QUESTION = data["question"]
        cls.OPTION = data["option"]
        cls.TYPE = data["type"]
        cls.A = data["a"]
        cls.QUIZ_NAME = data["quiz_name"]
        cls.ALL_QUESTIONS = data["all_questions"]

        cls.MOVIE = data["movie"]
        cls.MUSIC = data["music"]
        cls.BOOK = data["book"]

        cls.PERFORMER = data["performer"]

        cls.OPTIONS_JSON = data["options_json"]
        cls.QUESTION_TEXT = data["question_text"]
        cls.QUESTION_ID = data["question_id"]
        cls.IS_CORRECT = data["is_correct"]

        cls.ARRAY = data["array"]

        cls.TYPE_ID = data["type_id"]
        cls.TYPE_NAME = data["type_name"]
