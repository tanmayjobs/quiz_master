from src.controller.authentication import sign_in, sign_up
from src.helpers.constants import ScreenTexts, Output, Error
from src.helpers.common import invalid_choice, exit, show_message
from src.screens.home import home_screen


def sign_in_screen():
    username, password = ..., ...
    user = sign_in(username, password)

    if user:
        home_screen()


def sign_up_screen():
    username, password = ..., ...
    is_user_added = sign_up(username, password)
    if is_user_added:
        show_message(Output.USER_CREATED)
    else:
        show_message(Error.USERNAME_ALREADY_EXISTS)


def authentication_screen():
    user_choice = input(ScreenTexts.AUTHENTICATION)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:
            case 1:
                sign_in_screen()

            case 2:
                sign_up_screen()

            case 3:
                exit()

            case other:
                invalid_choice()

    else:
        invalid_choice()
