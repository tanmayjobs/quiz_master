from controller.questions import QuestionHandler
from helpers.constants import InputTexts, Numbers, OutputTexts
from data_containers.question import Question, Option


def correct_option_screen():
    print()
    correct_option = input(InputTexts.CORRECT_OPTION)

    if correct_option.isdigit():
        correct_option = int(correct_option)

        if not Numbers.ONE < correct_option > Numbers.FOUR:
            return correct_option

        else:
            print(OutputTexts.INVALID_CHOICE)

    else:
        print(OutputTexts.INVALID_CHOICE)

    return None


def add_question_screen(user, quiz):
    print()
    question_text = None

    while not question_text:
        question_text = input(InputTexts.QUESTION)

    options = []

    for option_no in range(Numbers.ONE, Numbers.FIVE):
        option_text = None

        while not option_text:
            option_text = input(InputTexts.OPTION.format(option_no)).strip()

        option = Option(option_text, False)
        options.append(option)

    correct_option = None
    while not correct_option:
        correct_option = correct_option_screen()

    options[correct_option - Numbers.ONE].is_correct = True
    question = Question(Numbers.ZERO, question_text, options)

    QuestionHandler(quiz.quiz_id, user).add_question(question)

    print(OutputTexts.QUESTION_ADDED)
