from constants import OutputTexts, Strings, InputTexts, Messages, Numbers
from controller.quiz import get_creator_quizzes, get_quiz_questions, get_random_quiz
from data_containers.question import Option
from helpers.common import newline, invalid_choice, show_quiz, show_message


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
        show_message(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        invalid_choice()
        return

    return selected_quiz


def show_question_info():
    ...


def ask_question(question_no, question):
    answer = input(question.prompt(question_no))

    if answer.isdigit():
        answer = int(answer)

        if Numbers.ONE <= answer <= Numbers.FOUR:
            return question.options[answer - Numbers.ONE]

        else:
            invalid_choice()

    else:
        invalid_choice()


def play_quiz(all_questions):
    player_score = 0

    for question_no, question in enumerate(all_questions, start=1):
        answer: Option | None = None

        while not answer:
            answer = ask_question(question_no, question)

        player_score += 1 if answer.is_correct else 0

    return player_score


def play_quiz_screen(player, quiz):
    newline()
    show_message(Messages.QUIZ_NAME.format(quiz.quiz_name))
    newline()

    all_questions = get_quiz_questions(quiz)

    if not all_questions:
        show_message(Messages.WORKING_ON_QUIZ)
        return

    player_score = play_quiz(all_questions)


def play_random_quiz(player):
    quiz = get_random_quiz()
    play_quiz_screen(player, quiz)
