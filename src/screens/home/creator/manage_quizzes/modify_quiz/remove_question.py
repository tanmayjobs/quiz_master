from constants import OutputTexts, Strings
from controller.quiz import get_quiz_questions
from data_containers.question import Question
from helpers.common import newline, show_message, show_question


def show_questions_info(all_questions: list[Question]):
    show_message(
        OutputTexts.QUESTION_INFO.format(
            question_id=Strings.ID,
            question_text=Strings.QUESTION
        )
    )

    for index, question in enumerate(all_questions, start=1):
        show_question(index, question)


def remove_question_screen(creator, quiz):
    newline()

    all_questions = get_quiz_questions(quiz)
    show_questions_info(all_questions)
