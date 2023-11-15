
class InputTexts:
    USERNAME = None
    PASSWORD = None
    USER_ID = None
    QUIZ_ID = None
    QUESTION_ID = None
    TYPE_IDS = None
    QUIZ_NAME = None
    QUESTION = None
    OPTION = None
    CORRECT_OPTION = None
    NUMBER_OF_QUESTIONS = None
    NUMBER_OF_OPTIONS = None
    QUESTION_PROMPT = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME = data["username"]
        cls.PASSWORD = data["password"]
        cls.USER_ID = data["user_id"]
        cls.QUIZ_ID = data["quiz_id"]
        cls.TYPE_IDS = data["type_ids"]
        cls.QUIZ_NAME = data["quiz_name"]
        cls.QUESTION = data["question"]
        cls.QUESTION_ID = data["question_id"]
        cls.OPTION = data["option"]
        cls.CORRECT_OPTION = data["correct_option"]
        cls.NUMBER_OF_QUESTIONS = data["number_of_questions"]
        cls.NUMBER_OF_OPTIONS = data["number_of_options"]
        cls.QUESTION_PROMPT = data["question_prompt"]
