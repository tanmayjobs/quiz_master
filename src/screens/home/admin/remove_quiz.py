from controller.quiz import QuizHandler
from helpers.constants import OutputTexts
from screens.home_screen.common import select_quiz_screen


def remove_quiz_screen(user):
    all_quizzes = QuizHandler(user).get_all_quizzes()
    quiz_to_remove = select_quiz_screen(all_quizzes)

    if not quiz_to_remove:
        return

    QuizHandler(user, quiz_to_remove).remove_quiz()

    print()
    print(OutputTexts.QUIZ_REMOVED)
