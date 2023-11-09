class ScreenTexts:
    AUTHENTICATION = None
    PLAYER_HOME = None
    CREATOR_HOME = None
    ADMIN_HOME = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__init__(cls, *args, **kwargs)

    @classmethod
    def __init__(cls, json_data):
        cls.AUTHENTICATION = json_data["authentication"]
        cls.PLAYER_HOME = json_data["home"]["player"]
        cls.CREATOR_HOME = json_data["home"]["creator"]
        cls.ADMIN_HOME = json_data["home"]["admin"]
