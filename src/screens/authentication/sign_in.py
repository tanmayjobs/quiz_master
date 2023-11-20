import controller.auth as auth_controller

from constants import Errors, InputTexts, LogText
from screens.common import show_message, password_input, newline, greet_user
from log.logger import Logger, WARN
from screens.home.home import home_screen


def sign_in_screen():
    newline()
    username, password = input(InputTexts.USERNAME).strip(), password_input()

    if not username:
        show_message(Errors.USERNAME_EMPTY)
        return

    if not password:
        show_message(Errors.PASSWORD_EMPTY)
        return

    user = auth_controller.sign_in(username, password)

    if user:
        greet_user(user)
        home_screen(user)
    else:
        Logger.log(WARN, LogText.INVALID_CREDENTIALS.format(username))
        show_message(Errors.INVALID_CREDENTIALS)
