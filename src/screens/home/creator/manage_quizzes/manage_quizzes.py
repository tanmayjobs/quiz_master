from constants import ScreenTexts
from helpers.common import newline, invalid_choice
from helpers.menu_loop import menu_loop
from screens.home.creator.manage_quizzes.add_quiz import add_quiz_screen
from screens.home.creator.manage_quizzes.modify_quiz.modify_quiz import modify_quiz_screen
from screens.home.creator.manage_quizzes.remove_quiz import remove_quiz


def select_modify_quiz(creator):
    ...


@menu_loop
def manage_quizzes_screen(creator):
    newline()
    user_choice = input(ScreenTexts.MANAGE_QUIZZES)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                add_quiz_screen(creator)

            case 2:
                remove_quiz(creator)

            case 3:
                select_modify_quiz(creator)

            case 4:
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False