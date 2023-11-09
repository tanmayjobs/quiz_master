class Messages:
    QUIZ_NAME = None
    QUIZ_TYPE = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.QUIZ_NAME = json_data["quiz_name"]
        cls.QUIZ_TYPE = json_data["quiz_type"]
