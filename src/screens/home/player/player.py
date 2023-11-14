from constants import ScreenTexts
from helpers.common import invalid_choice, newline
from helpers.menu_loop import menu_loop


@menu_loop
def player_home_screen(user):
    newline()
    user_choice = input(ScreenTexts.PLAYER_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                ...

            case 2:
                ...

            case 3:
                ...

            case 4:
                ...  # sign out
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
