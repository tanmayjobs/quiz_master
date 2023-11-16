from screens.authentication.sign_in import sign_in_screen
from screens.authentication.sign_up import sign_up_screen

from constants import ScreenTexts
from helpers.common import invalid_choice, quit_application, newline
from helpers.menu_loop import menu_loop


@menu_loop
def authentication_screen():
    newline()
    user_choice = input(ScreenTexts.AUTHENTICATION)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:
            case 1:
                sign_in_screen()

            case 2:
                sign_up_screen()

            case 3:
                quit_application()

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
