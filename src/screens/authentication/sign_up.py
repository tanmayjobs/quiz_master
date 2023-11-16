from controller.user import sign_up
from constants import OutputTexts, Errors, InputTexts
from helpers.common import show_message, password_input, newline


def sign_up_screen():
    newline()
    username, password = input(InputTexts.USERNAME), password_input()
    username = username.strip()

    if not username:
        show_message(Errors.USERNAME_EMPTY)
        return

    if not password:
        show_message(Errors.PASSWORD_EMPTY)
        return

    is_user_added = sign_up(username, password)

    if is_user_added:
        show_message(OutputTexts.USER_ADDED)
    else:
        show_message(Errors.USERNAME_ALREADY_EXISTS)
