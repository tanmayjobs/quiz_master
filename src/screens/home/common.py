from constants import OutputTexts, Strings, InputTexts
from controller.quiz import get_creator_quizzes
from helpers.common import newline, invalid_choice, show_quiz, show_message


def remove_quiz_screen(user):
    ...


def show_all_quizzes(all_quizzes):
    show_message(
        OutputTexts.QUIZ_INFO.format(
            quiz_id=Strings.ID,
            quiz_name=Strings.QUIZ,
            quiz_types=Strings.TYPE,
        )
    )

    for index, quiz in enumerate(all_quizzes, start=1):
        show_quiz(index, quiz)


def select_quiz(all_quizzes):
    index = input(InputTexts.QUIZ_ID)

    if not index.isdigit():
        return None

    index = int(index) - 1

    if index < 0 or index > len(all_quizzes) - 1:
        return None

    return all_quizzes[index]


def select_quiz_screen(creator):
    newline()
    all_quizzes = get_creator_quizzes(performer=creator)

    if not all_quizzes:
        show_message()
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        invalid_choice()
        return

    return selected_quiz


def show_question_info():
    ...
