from constants import InputTexts, Numbers, OutputTexts
from controller.quiz import add_question
from data_containers.question import Question, Option
from helpers.common import newline, invalid_choice, show_message


def correct_option_screen():
    newline()
    correct_option = input(InputTexts.CORRECT_OPTION)

    if correct_option.isdigit():
        correct_option = int(correct_option)

        if not Numbers.ONE < correct_option > Numbers.FOUR:
            return correct_option

        else:
            invalid_choice()

    else:
        invalid_choice()

    return None


def add_question_screen(creator, quiz):
    newline()
    question_text = input(InputTexts.QUESTION)
    options = []

    for option_no in range(Numbers.ONE, Numbers.FIVE):
        option_text = input(InputTexts.OPTION.format(option_no))

        option = Option(option_text, False)
        options.append(option)

    correct_option = None
    while not correct_option:
        correct_option = correct_option_screen()

    options[correct_option - 1].is_correct = True
    question = Question(question_text, options)

    add_question(quiz, question, performer=creator)

    show_message(OutputTexts.QUESTION_ADDED)
