import re
import pwinput

from helpers.constants import InputTexts, Errors
from helpers.constants.regex_patterns import RegexPatterns
from utils.until_not_valid import until_not_valid


class Validators:
    """
    This class provides a way out of invalid user inputs.
    Each method uses regex to validate the user input based on the needs.
    """

    @staticmethod
    @until_not_valid
    def get_username():
        username = input(InputTexts.USERNAME).strip()
        if not re.match(RegexPatterns.USERNAME, username):
            print(Errors.INVALID_INPUT)
            username = ''
        return username

    @staticmethod
    @until_not_valid
    def get_password():
        password = pwinput.pwinput(InputTexts.PASSWORD)
        if not re.match(RegexPatterns.PASSWORD, password):
            print(Errors.WEAK_PASSWORD)
            password = ''
        return password

    @staticmethod
    @until_not_valid
    def get_valid_strings(prompt):
        string = input(prompt).strip()
        if not re.match(RegexPatterns.ALPHA_NUM_Q2, string):
            print(Errors.INVALID_INPUT)
            string = ''
        return string

    @staticmethod
    @until_not_valid
    def get_correct_option():
        correct_option = input(InputTexts.CORRECT_OPTION).strip()
        if not re.match(RegexPatterns.CORRECT_OPTION, correct_option):
            print(Errors.INVALID_INPUT)
            correct_option = ''
            return correct_option

        return int(correct_option) - 1
