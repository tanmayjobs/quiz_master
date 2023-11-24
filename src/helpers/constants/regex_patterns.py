class RegexPatterns:
    USERNAME = None
    PASSWORD = None
    ALPHA_NUM_Q3 = None
    CORRECT_OPTION = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME = data["username"]
        cls.PASSWORD = data["password"]
        cls.ALPHA_NUM_Q3 = data["alpha_num_q3"]
        cls.CORRECT_OPTION = data["correct_option"]
