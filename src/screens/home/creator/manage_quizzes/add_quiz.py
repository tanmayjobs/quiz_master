from constants import InputTexts, OutputTexts, Strings
from controller.quiz import add_quiz, all_quiz_types
from data_containers.quiz import Quiz
from data_containers.user import User

from helpers.common import newline, invalid_choice, show_message, show_type


def show_all_types(all_types):
    show_message(
        OutputTexts.TYPE_INFO.format(
            type_id=Strings.ID,
            type_name=Strings.TYPE
        )
    )

    for index, each_type in enumerate(all_types, start=1):
        show_type(index, each_type)


def select_types(all_types):
    indexes = input(InputTexts.TYPE_IDS).split(",")

    if not indexes:
        return None

    selected_types = []

    for index in indexes:
        if not index.isdigit():
            return None

        index = int(index) - 1

        if index < 0 or index > len(all_types) - 1:
            return None

        selected_types.append(all_types[index])

    return selected_types


def quiz_type_screen():
    all_types = all_quiz_types()
    show_all_types(all_types)

    selected_types = select_types(all_types)

    if not selected_types:
        invalid_choice()
        newline()
        return None

    return selected_types


def add_quiz_screen(creator: User):
    newline()

    quiz_name = input(InputTexts.QUIZ_NAME)

    quiz_types = None
    while not quiz_types:
        quiz_types = quiz_type_screen()

    quiz = Quiz(
        quiz_id=None,
        quiz_name=quiz_name,
        creator_id=creator.user_id,
        creator_name=creator.username,
        types=quiz_types
    )

    add_quiz(quiz, performer=creator)

    newline()
    show_message(OutputTexts.QUIZ_ADDED)
