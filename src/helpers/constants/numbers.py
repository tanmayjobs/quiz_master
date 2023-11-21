class Numbers:
    ZERO = None
    ONE = None
    TWO = None
    FOUR = None
    FIVE = None
    SIX = None
    TEN = None

    @classmethod
    def __init__(cls, data):
        cls.ZERO = data["zero"]
        cls.ONE = data["one"]
        cls.TWO = data["two"]
        cls.FOUR = data["four"]
        cls.FIVE = data["five"]
        cls.SIX = data["six"]
        cls.TEN = data["ten"]
