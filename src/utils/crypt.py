import re

import bcrypt

from helpers.constants.regex_patterns import RegexPatterns


def hash_password(password: str):
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)

    return password_hash


def check_password(password: str, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)


def validate_password(password):
    return re.match(RegexPatterns.PASSWORD, password)
