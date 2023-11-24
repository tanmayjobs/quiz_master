import re

import pwinput

from helpers.constants import Strings, InputTexts, OutputTexts, Errors
from helpers.constants.regex_patterns import RegexPatterns


class Validators:
    @staticmethod
    def get_username():
        username = ''
        while not username:
            username = input(InputTexts.USERNAME).strip()
            if not re.match(RegexPatterns.USERNAME, username):
                print(Errors.INVALID_INPUT)
                username = ''
        return username

    @staticmethod
    def get_password():
        password = ''
        while not password:
            password = pwinput.pwinput(InputTexts.PASSWORD)
            if not re.match(RegexPatterns.PASSWORD, password):
                print(Errors.WEAK_PASSWORD)
                password = ''
        return password

    @staticmethod
    def get_valid_strings(prompt):
        string = ''
        while not string:
            string = input(prompt).strip()
            if not re.match(RegexPatterns.ALPHA_NUM_Q3, string):
                print(Errors.INVALID_INPUT)
                string = ''
        return string

    @staticmethod
    def get_correct_option():
        correct_option = ''
        while not correct_option:
            correct_option = input(InputTexts.CORRECT_OPTION).strip()
            if not re.match(RegexPatterns.CORRECT_OPTION, correct_option):
                print(Errors.INVALID_INPUT)
                correct_option = ''
        return int(correct_option) - 1
