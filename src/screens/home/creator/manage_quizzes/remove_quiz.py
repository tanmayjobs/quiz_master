from constants import OutputTexts, InputTexts
from controller.quiz import remove_quiz
from helpers.common import show_message, newline, invalid_choice
from screens.home.common import select_creator_quiz_screen


def remove_quiz_screen(creator):
    quiz_to_remove = select_creator_quiz_screen(creator)

    if not quiz_to_remove:
        return

    remove_quiz(quiz_to_remove, performer=creator)

    newline()
    show_message(OutputTexts.QUIZ_REMOVED)
