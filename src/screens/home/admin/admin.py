from helpers.constants import ScreenTexts, OutputTexts
from utils.menu_loop import menu_loop
from screens.home_screen.admin.add_creator import add_creator_screen
from screens.home_screen.admin.remove_quiz import remove_quiz_screen
from screens.home_screen.admin.remove_user import remove_user_screen


@menu_loop
def admin_home_screen(user):
    print()
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
                print(OutputTexts.INVALID_CHOICE)

    else:
        print(OutputTexts.INVALID_CHOICE)

    return False
