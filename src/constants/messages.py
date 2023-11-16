class Messages:
    QUIZ_NAME = None
    QUIZ_TYPE = None
    CREATOR_INFO = None
    WORKING_ON_QUIZ = None
    GREET = None
    INCORRECT_GUESS = None
    CORRECT_GUESS = None
    TOP_RECORD = None

    @classmethod
    def __init__(cls, data):
        cls.QUIZ_NAME = data["quiz_name"]
        cls.QUIZ_TYPE = data["quiz_type"]
        cls.CREATOR_INFO = data["creator_info"]
        cls.WORKING_ON_QUIZ = data["working_on_quiz"]
        cls.GREET = data["greet"]
        cls.INCORRECT_GUESS = data["incorrect_guess"]
        cls.CORRECT_GUESS = data["correct_guess"]
        cls.TOP_RECORD = data["top_record"]
