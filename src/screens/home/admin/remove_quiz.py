from constants import OutputTexts, Strings
from controller.quiz import get_all_quizzes, remove_quiz
from helpers.common import newline, invalid_choice, show_message
from screens.home.common import show_all_quizzes, select_quiz


def select_quiz_screen(admin):
    newline()
    all_quizzes = get_all_quizzes(performer=admin)

    if not all_quizzes:
        show_message(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        invalid_choice()
        return

    return selected_quiz


def remove_quiz_screen(admin):
    quiz_to_remove = select_quiz_screen(admin)

    if not quiz_to_remove:
        return

    remove_quiz(quiz_to_remove, performer=admin)

    newline()
    show_message(OutputTexts.QUIZ_REMOVED)
