class SQLQueries:
    CREATE_AUTH_TABLE = None
    CREATE_QUIZ_TABLE = None
    CREATE_QUESTION_TABLE = None
    CREATE_OPTION_TABLE = None
    CREATE_QUIZ_SCORE_TABLE = None
    CREATE_TYPE_TABLE = None
    CREATE_QUIZ_TYPE_MAPPING_TABLE = None

    GET_ALL_USERS = None
    GET_USER = None
    ADD_USER = None
    REMOVE_USER = None

    @classmethod
    def __init__(cls, data):
        cls.CREATE_AUTH_TABLE = data["create_auth_table"]
        cls.CREATE_QUIZ_TABLE = data["create_quiz_table"]
        cls.CREATE_QUESTION_TABLE = data["create_question_table"]
        cls.CREATE_OPTION_TABLE = data["create_option_table"]
        cls.CREATE_QUIZ_SCORE_TABLE = data["create_quiz_score_table"]
        cls.CREATE_TYPE_TABLE = data["create_type_table"]
        cls.CREATE_QUIZ_TYPE_MAPPING_TABLE = data["create_quiz_type_mapping_table"]

        cls.GET_ALL_USERS = data["get_all_users"]
        cls.GET_USER = data["get_user"]
        cls.ADD_USER = data["add_user"]
        cls.REMOVE_USER = data["remove_user"]
