from controller.user import sign_in
from constants import Errors, InputTexts
from helpers.common import show_message, password_input, newline
from screens.home.home import home_screen


def sign_in_screen():
    newline()
    username, password = input(InputTexts.USERNAME), password_input()
    user = sign_in(username, password)

    if user:
        home_screen(user)
    else:
        show_message(Errors.INVALID_CREDENTIALS)
