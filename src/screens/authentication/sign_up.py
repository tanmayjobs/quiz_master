import controller.auth as auth_controller

from constants import OutputTexts, Errors, InputTexts
from screens.common import show_message, password_input, newline, validate_password


def sign_up_screen():
    newline()
    username, password = input(InputTexts.USERNAME), password_input()
    username = username.strip()

    if not username:
        show_message(Errors.USERNAME_EMPTY)
        return

    if not validate_password(password):
        show_message(Errors.WEAK_PASSWORD)
        return

    is_user_added = auth_controller.sign_up(username, password)

    if is_user_added:
        show_message(OutputTexts.USER_ADDED)
    else:
        show_message(Errors.USERNAME_ALREADY_EXISTS)
