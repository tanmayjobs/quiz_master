from constants import InputTexts, Numbers, OutputTexts, Strings
from controller.quiz import add_quiz, all_quiz_types
from data_containers.question import Question
from data_containers.quiz import Quiz
from data_containers.user import User

from helpers.common import newline, invalid_choice, show_message, show_user, show_type


def create_options():
    options = []

    for option_no in range(Numbers.ONE, Numbers.FIVE):
        option = input(InputTexts.OPTION.format(option_no))
        options.append(option)

    return options


def correct_option_screen():
    correct_option = input(InputTexts.CORRECT_OPTION)

    if correct_option.isdigit():
        correct_option = int(correct_option)

        if correct_option < Numbers.ONE or correct_option > Numbers.FOUR:
            invalid_choice()

        else:
            return correct_option
    else:
        invalid_choice()


def create_question_screen():
    newline()

    question = Question(options={})

    question_val = input(InputTexts.QUESTION)
    question.question = question_val

    options = create_options()
    correct_option = None

    while not correct_option:
        correct_option = correct_option_screen()

    for index, option in enumerate(options, start=Numbers.ONE):
        question.add_option(option, index == correct_option)

    return question


def create_questions(number_of_questions):
    all_questions = []
    for _ in range(number_of_questions):
        create_question_screen()

    return all_questions


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
