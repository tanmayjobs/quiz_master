class Messages:
    QUIZ_NAME = None
    QUIZ_TYPE = None

    @classmethod
    def __init__(cls, data):
        cls.QUIZ_NAME = data["quiz_name"]
        cls.QUIZ_TYPE = data["quiz_type"]
