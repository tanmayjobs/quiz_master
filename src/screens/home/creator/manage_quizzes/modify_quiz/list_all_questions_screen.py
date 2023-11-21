from controller.questions import QuestionHandler
from helpers.constants import OutputTexts, Strings
from screens.common import show_questions_all_info


def list_all_questions_screen(quiz):
    print()

    all_questions = QuestionHandler(quiz.quiz_id).get_quiz_questions()

    if not all_questions:
        print(OutputTexts.NOT_YET.format(Strings.QUESTION))
        return

    for index, question in enumerate(all_questions, start=1):
        show_questions_all_info(index, question)
        print()

    print()
