from controller.quiz import QuizHandler
from helpers.constants import OutputTexts
from screens.home_screen.common import select_creator_quiz_screen


def remove_quiz_screen(user):
    quiz_to_remove = select_creator_quiz_screen(user)

    if not quiz_to_remove:
        return

    QuizHandler(user, quiz_to_remove).remove_quiz()

    print()
    print(OutputTexts.QUIZ_REMOVED)
