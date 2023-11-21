from helpers.constants import ScreenTexts, OutputTexts
from utils.menu_loop import menu_loop
from screens.home_screen.common import select_creator_quiz_screen
from screens.home_screen.creator.manage_quizzes.add_quiz import add_quiz_screen
from screens.home_screen.creator.manage_quizzes.modify_quiz.modify_quiz import modify_quiz_screen
from screens.home_screen.creator.manage_quizzes.remove_quiz import remove_quiz_screen


@menu_loop
def manage_quizzes_screen(creator):
    print()
    user_choice = input(ScreenTexts.MANAGE_QUIZZES)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                add_quiz_screen(creator)

            case 2:
                remove_quiz_screen(creator)

            case 3:
                selected_quiz = select_creator_quiz_screen(creator)

                if selected_quiz:
                    modify_quiz_screen(creator, selected_quiz)

            case 4:
                return True

            case other:
                print(OutputTexts.INVALID_CHOICE)

    else:
        print(OutputTexts.INVALID_CHOICE)

    return False
