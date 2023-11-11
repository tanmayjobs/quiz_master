from constants import ScreenTexts
from helpers.common import invalid_choice
from helpers.menu_loop import menu_loop


@menu_loop
def creator_home_screen(user):
    user_choice = input(ScreenTexts.CREATOR_HOME)

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
                ...

            case 5:
                ...  # sign out
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
