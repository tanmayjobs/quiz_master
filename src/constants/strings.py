class Strings:
    ADMIN = None
    CREATOR = None
    PLAYER = None
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

    @classmethod
    def __init__(cls, data):
        cls.ADMIN = data["admin"]
        cls.CREATOR = data["creator"]
        cls.PLAYER = data["player"]
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
