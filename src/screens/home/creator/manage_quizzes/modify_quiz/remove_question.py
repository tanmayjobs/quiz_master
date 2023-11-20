from constants import OutputTexts, Strings, InputTexts
from controller.quiz import get_quiz_questions, remove_question
from data_containers.question import Question
from screens.common import newline, show_message, show_question, invalid_choice


def select_question(all_question):
    index = input(InputTexts.QUESTION_ID)

    if not index.isdigit():
        return None

    index = int(index) - 1

    if index < 0 or index > len(all_question) - 1:
        return None

    return all_question[index]


def show_questions_info(all_questions: list[Question], all_info=False):
    info_message = OutputTexts.QUESTION_INFO if not all_info else OutputTexts.QUESTION_ALL_INFO

    show_message(
        info_message.format(
            question_id=Strings.ID,
            question_text=Strings.QUESTION
        )
    )

    for index, question in enumerate(all_questions, start=1):
        show_question(index, question)


def remove_question_screen(creator, quiz):
    newline()

    all_questions = get_quiz_questions(quiz)

    if not all_questions:
        show_message(OutputTexts.NOT_YET.format(Strings.QUESTION))
        return

    show_questions_info(all_questions)

    selected_question = select_question(all_questions)

    if not selected_question:
        invalid_choice()
        return

    remove_question(selected_question, performer=creator)
    newline()
    show_message(OutputTexts.QUESTION_REMOVED)
