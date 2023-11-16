from controller.user import sign_in
from constants import Errors, InputTexts, LogText
from helpers.common import show_message, password_input, newline, greet_user
from log.logger import Logger, WARN
from screens.home.home import home_screen


def sign_in_screen():
    newline()
    username, password = input(InputTexts.USERNAME), password_input()
    user = sign_in(username, password)

    if user:
        greet_user(user)
        home_screen(user)
    else:
        Logger.log(WARN, LogText.INVALID_CREDENTIALS.format(username))
        show_message(Errors.INVALID_CREDENTIALS)
