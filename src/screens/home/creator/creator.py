from constants import ScreenTexts
from helpers.common import invalid_choice, newline
from helpers.menu_loop import menu_loop
from screens.home.common import play_random_quiz, show_records_screen
from screens.home.creator.manage_quizzes.manage_quizzes import manage_quizzes_screen


@menu_loop
def creator_home_screen(creator):
    newline()
    user_choice = input(ScreenTexts.CREATOR_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                play_random_quiz(creator)

            case 2:
                ...

            case 3:
                show_records_screen(creator)

            case 4:
                manage_quizzes_screen(creator)

            case 5:
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
