from controller.user import sign_in
from constants import Errors, InputTexts, LogText
from helpers.common import show_message, password_input, newline
from log.logger import Logger, WARN
from screens.home.home import home_screen


def sign_in_screen():
    newline()
    username, password = input(InputTexts.USERNAME), password_input()
    user = sign_in(username, password)

    if user:
        home_screen(user)
    else:
        Logger.log(WARN, LogText.INVALID_CREDENTIALS)
        show_message(Errors.INVALID_CREDENTIALS)
