import pwinput

from helpers.constants import InputTexts, Errors
from utils.until_not_valid import until_not_valid
import utils.validators as Validators


@until_not_valid
def get_username():
    username = Validators.get_username(input(InputTexts.USERNAME))
    if not username:
        print(Errors.INVALID_INPUT)

    return username

@until_not_valid
def get_password():
    password = Validators.get_password(pwinput.pwinput(InputTexts.PASSWORD))
    if not password:
        print(Errors.WEAK_PASSWORD)

    return password


@until_not_valid
def get_string(prompt):
    string = Validators.get_valid_strings(input(prompt))
    if not string:
        print(Errors.INVALID_INPUT)

    return None


@until_not_valid
def get_correct_option():
    correct_option = Validators.get_correct_option(input(InputTexts.CORRECT_OPTION))
    if not correct_option:
        print(Errors.INVALID_INPUT)

    return None
