from controller.authentication import sign_in, sign_up
from constants import ScreenTexts, OutputTexts, Errors, InputTexts
from helpers.common import invalid_choice, quit, show_message, password_input, new_line
from helpers.menu_loop import menu_loop
from screens.home import home_screen


def sign_in_screen():
    new_line()
    username, password = input(InputTexts.USERNAME), password_input()
    user = sign_in(username, password)

    if user:
        home_screen(user)
    else:
        show_message(Errors.INVALID_CREDENTIALS)
    new_line()


def sign_up_screen():
    new_line()
    username, password = input(InputTexts.USERNAME), password_input()
    is_user_added = sign_up(username, password)

    if is_user_added:
        show_message(OutputTexts.USER_CREATED)
    else:
        show_message(Errors.USERNAME_ALREADY_EXISTS)


@menu_loop
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
                quit()

            case other:
                invalid_choice()

    else:
        invalid_choice()
