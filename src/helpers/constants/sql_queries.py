class SQLQueries:
    CREATE_AUTH_TABLE = None
    CREATE_QUIZ_TABLE = None
    CREATE_QUESTION_TABLE = None
    CREATE_OPTION_TABLE = None
    CREATE_QUIZ_SCORE_TABLE = None
    CREATE_TYPE_TABLE = None
    CREATE_QUIZ_TYPE_MAPPING_TABLE = None

    GET_ALL_TYPES = None
    ADD_QUIZ_TYPE = None
    ADD_TYPE = None

    GET_ALL_USERS = None
    GET_USER = None
    ADD_USER = None
    REMOVE_USER = None

    ADD_QUIZ = None
    ADD_QUESTION = None
    ADD_OPTION = None
    REMOVE_QUIZ = None

    GET_USER_QUIZZES = None
    GET_QUIZ_TYPES = None
    GET_QUIZ_QUESTIONS = None
    GET_RANDOM_QUIZ = None

    REMOVE_QUESTION = None
    REMOVE_OPTION_BY_QUESTION = None

    GET_ALL_QUIZZES = None
    FILTER_ALL_QUIZZES = None

    ADD_QUIZ_SCORE = None
    GET_PLAYER_SCORES = None
    TOP_QUIZ_SCORES = None

    @classmethod
    def __init__(cls, data):
        cls.CREATE_AUTH_TABLE = data["create_auth_table"]
        cls.CREATE_QUIZ_TABLE = data["create_quiz_table"]
        cls.CREATE_QUESTION_TABLE = data["create_question_table"]
        cls.CREATE_OPTION_TABLE = data["create_option_table"]
        cls.CREATE_QUIZ_SCORE_TABLE = data["create_quiz_score_table"]
        cls.CREATE_TYPE_TABLE = data["create_type_table"]
        cls.CREATE_QUIZ_TYPE_MAPPING_TABLE = data[
            "create_quiz_type_mapping_table"]

        cls.GET_ALL_TYPES = data["get_all_types"]
        cls.ADD_QUIZ_TYPE = data["add_quiz_type"]
        cls.ADD_TYPE = data["add_type"]

        cls.GET_ALL_USERS = data["get_all_users"]
        cls.GET_USER = data["get_user"]
        cls.ADD_USER = data["add_user"]
        cls.ADD_QUIZ = data["add_quiz"]
        cls.REMOVE_QUIZ = data["remove_quiz"]
        cls.REMOVE_USER = data["remove_user"]

        cls.GET_USER_QUIZZES = data["get_user_quizzes"]
        cls.GET_QUIZ_TYPES = data["get_quiz_types"]
        cls.GET_QUIZ_QUESTIONS = data["get_quiz_questions"]
        cls.GET_RANDOM_QUIZ = data["get_random_quiz"]

        cls.ADD_QUESTION = data["add_question"]
        cls.ADD_OPTION = data["add_option"]
        cls.TOP_QUIZ_SCORES = data["top_quiz_scores"]

        cls.REMOVE_QUESTION = data["remove_question"]
        cls.REMOVE_OPTION_BY_QUESTION = data["remove_option_by_question"]

        cls.GET_ALL_QUIZZES = data["get_all_quizzes"]
        cls.ADD_QUIZ_SCORE = data["add_quiz_score"]
        cls.GET_PLAYER_SCORES = data["get_player_scores"]

        cls.FILTER_ALL_QUIZZES = data["filter_all_quizzes"]
