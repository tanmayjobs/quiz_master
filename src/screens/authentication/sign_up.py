from controller.user import sign_up
from constants import OutputTexts, Errors, InputTexts
from helpers.common import show_message, password_input, new_line


def sign_up_screen():
    new_line()
    username, password = input(InputTexts.USERNAME), password_input()
    is_user_added = sign_up(username, password)

    if is_user_added:
        show_message(OutputTexts.USER_ADDED)
    else:
        show_message(Errors.USERNAME_ALREADY_EXISTS)
