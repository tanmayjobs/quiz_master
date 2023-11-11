from constants import ScreenTexts

from helpers.common import invalid_choice
from helpers.menu_loop import menu_loop

from screens.home.admin.add_creator import add_creator_screen
from screens.home.admin.remove_user import remove_user_screen
from screens.home.common import remove_quiz_screen


@menu_loop
def admin_home_screen(user):
    user_choice = input(ScreenTexts.ADMIN_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                add_creator_screen(user)

            case 2:
                remove_user_screen(user)

            case 3:
                remove_quiz_screen(user)

            case 4:
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
