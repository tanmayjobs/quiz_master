from constants import OutputTexts, Strings
from controller.quiz import get_quiz_questions
from screens.common import newline, show_message, show_questions_all_info


def list_all_questions_screen(quiz):
    newline()

    all_questions = get_quiz_questions(quiz)

    if not all_questions:
        show_message(OutputTexts.NOT_YET.format(Strings.QUESTION))
        return

    for index, question in enumerate(all_questions, start=1):
        show_questions_all_info(index, question)
        newline()

    newline()