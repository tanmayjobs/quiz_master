from constants import OutputTexts
from helpers.common import show_message, newline
from screens.home.common import select_quiz_screen


def remove_quiz(creator):
    quiz_to_remove = select_quiz_screen(creator)
    newline()
    show_message(OutputTexts.QUIZ_REMOVED)
