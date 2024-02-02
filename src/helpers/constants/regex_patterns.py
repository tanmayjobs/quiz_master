class RegexPatterns:
    USERNAME = "^[a-zA-Z][a-zA-Z0-9]{1,20}$"
    PASSWORD = '^.*(?=.{6,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[@!#$%&? "]).*$'
    ALPHA_NUM_Q2 = "^.*[a-zA-Z0-9].*$"
