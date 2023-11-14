from constants import ScreenTexts
from helpers.common import newline, invalid_choice
from helpers.menu_loop import menu_loop
from screens.home.creator.manage_quizzes.modify_quiz.add_question import add_question_screen
from screens.home.creator.manage_quizzes.modify_quiz.remove_question import remove_question_screen


@menu_loop
def modify_quiz_screen(creator, quiz):
    newline()
    user_choice = input(ScreenTexts.MANAGE_QUIZ)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                add_question_screen(creator, quiz)

            case 2:
                remove_question_screen(creator, quiz)

            case 3:
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
