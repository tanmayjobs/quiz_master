class ScreenTexts:
    AUTHENTICATION = None
    PLAYER_HOME = None
    CREATOR_HOME = None
    ADMIN_HOME = None

    @classmethod
    def __init__(cls, data):
        cls.AUTHENTICATION = data["authentication"]
        cls.PLAYER_HOME = data["home"]["player"]
        cls.CREATOR_HOME = data["home"]["creator"]
        cls.ADMIN_HOME = data["home"]["admin"]
