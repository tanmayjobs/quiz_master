class Messages:
    QUIZ_NAME = None
    QUIZ_TYPE = None
    CREATOR_INFO = None
    WORKING_ON_QUIZ = None

    @classmethod
    def __init__(cls, data):
        cls.QUIZ_NAME = data["quiz_name"]
        cls.QUIZ_TYPE = data["quiz_type"]
        cls.CREATOR_INFO = data["creator_info"]
        cls.WORKING_ON_QUIZ = data["working_on_quiz"]
