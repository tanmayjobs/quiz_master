from constants import OutputTexts
from controller.quiz import get_all_quizzes, remove_quiz
from screens.common import newline, show_message
from screens.home.common import select_quiz_screen


def remove_quiz_screen(admin):
    all_quizzes = get_all_quizzes(performer=admin)
    quiz_to_remove = select_quiz_screen(all_quizzes)

    if not quiz_to_remove:
        return

    remove_quiz(quiz_to_remove, performer=admin)

    newline()
    show_message(OutputTexts.QUIZ_REMOVED)
