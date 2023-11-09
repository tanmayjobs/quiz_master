from src.controller.authentication import sign_in, sign_up
from src.helpers.constants import MenuTexts
from src.helpers.common import invalid_choice, exit


def sign_in_menu():
    username, password = ..., ...
    user = sign_in(username, password)

    if user:
        ...
    else:
        ...


def sign_up_menu():
    username, password = ..., ...
    is_user_added = sign_up(username, password)
    if is_user_added:
        ...
    else:
        ...


def authentication_menu():
    user_choice = input(MenuTexts.AUTHENTICATION)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:
            case 1:
                sign_in_menu()

            case 2:
                sign_up_menu()

            case 3:
                exit()

            case other:
                invalid_choice()

    else:
        invalid_choice()
