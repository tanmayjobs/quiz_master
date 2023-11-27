import re

from helpers.constants.regex_patterns import RegexPatterns

"""
This file provides a way out of invalid user inputs.
Each method uses regex to validate the user input based on the needs.
"""


def get_username(username):
    if not re.match(RegexPatterns.USERNAME, username):
        return None
    return username


def get_password(password):
    if not re.match(RegexPatterns.PASSWORD, password):
        return None
    return password


def get_valid_strings(string):
    if not re.match(RegexPatterns.ALPHA_NUM_Q2, string):
        return None
    return string


def get_correct_option(correct_option):
    if not re.match(RegexPatterns.CORRECT_OPTION, correct_option):
        return None
    return int(correct_option) - 1
