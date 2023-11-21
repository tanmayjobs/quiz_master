from controller.questions import QuestionHandler
from helpers.constants import OutputTexts, Strings, InputTexts
from data_containers.question import Question
from screens.common import show_question


def select_question(all_question) -> Question:
    index = input(InputTexts.QUESTION_ID)

    if not index.isdigit():
        return None

    index = int(index) - 1

    if index < 0 or index > len(all_question) - 1:
        return None

    return all_question[index]


def show_questions_info(all_questions: list[Question], all_info=False):
    info_message = OutputTexts.QUESTION_INFO if not all_info else OutputTexts.QUESTION_ALL_INFO

    print(
        info_message.format(
            question_id=Strings.ID,
            question_text=Strings.QUESTION
        )
    )

    for index, question in enumerate(all_questions, start=1):
        show_question(index, question)


def remove_question_screen(user, quiz):
    print()

    all_questions = QuestionHandler(quiz.quiz_id).get_quiz_questions()

    if not all_questions:
        print(OutputTexts.NOT_YET.format(Strings.QUESTION))
        return

    show_questions_info(all_questions)

    selected_question = select_question(all_questions)

    if not selected_question:
        print(OutputTexts.INVALID_CHOICE)
        return

    QuestionHandler(quiz.quiz_id, user).remove_question(selected_question.question_id)
    print()
    print(OutputTexts.QUESTION_REMOVED)
