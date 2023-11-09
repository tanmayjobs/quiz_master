import json


class SQLQueries:
    CREATE_AUTH_TABLE = None
    CREATE_QUIZ_TABLE = None
    CREATE_QUESTION_TABLE = None
    CREATE_OPTION_TABLE = None
    CREATE_QUIZ_SCORE_TABLE = None
    CREATE_TYPE_TABLE = None
    CREATE_QUIZ_TYPE_MAPPING_TABLE = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.CREATE_AUTH_TABLE = json_data["create_auth_table"]
        cls.CREATE_QUIZ_TABLE = json_data["create_quiz_table"]
        cls.CREATE_QUESTION_TABLE = json_data["create_question_table"]
        cls.CREATE_OPTION_TABLE = json_data["create_option_table"]
        cls.CREATE_QUIZ_SCORE_TABLE = json_data["create_quiz_score_table"]
        cls.CREATE_TYPE_TABLE = json_data["create_type_table"]
        cls.CREATE_QUIZ_TYPE_MAPPING_TABLE = json_data["create_quiz_type_mapping_table"]


class MenuTexts:
    AUTHENTICATION = None
    PLAYER_HOME = None
    CREATOR_HOME = None
    ADMIN_HOME = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.AUTHENTICATION = json["authentication"]
        cls.PLAYER_HOME = json["home"]["player"]
        cls.CREATOR_HOME = json["home"]["creator"]
        cls.ADMIN_HOME = json["home"]["admin"]


class Output:
    INVALID_CHOICE = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.INVALID_CHOICE = json["invalid_choice"]


class Messages:
    QUIZ_NAME = None
    QUIZ_TYPE = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.QUIZ_NAME = json["quiz_name"]
        cls.QUIZ_TYPE = json["quiz_type"]


def load_constants():
    with open("constants.yaml", "r") as constants_file:
        json_data = json.load(constants_file)
        SQLQueries(json_data["sql_queries"])
        MenuTexts(json_data["screens"])
        Output(json_data["output"])
        Messages(json_data["message"])
