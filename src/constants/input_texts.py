
class InputTexts:
    USERNAME = None
    PASSWORD = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME = data["username"]
        cls.PASSWORD = data["password"]

