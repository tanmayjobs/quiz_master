class RegexPatterns:
    USERNAME = None
    PASSWORD = None
    ALPHA_NUM_Q2 = None
    CORRECT_OPTION = None

    @classmethod
    def __init__(cls, data):
        cls.USERNAME = data["username"]
        cls.PASSWORD = data["password"]
        cls.ALPHA_NUM_Q2 = data["alpha_num_q2"]
        cls.CORRECT_OPTION = data["correct_option"]
