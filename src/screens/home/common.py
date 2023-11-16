from constants import OutputTexts, Strings, InputTexts, Messages, Numbers
from controller.quiz import get_creator_quizzes, get_quiz_questions, get_random_quiz, filter_all_quizzes
from controller.quiz_record import add_quiz_record, get_player_records

from data_containers.question import Option
from data_containers.quiz import Quiz
from data_containers.quiz_record import QuizRecord
from data_containers.user import User

from helpers.common import newline, invalid_choice, show_quiz, show_message, show_record


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


def select_creator_quiz_screen(creator):
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

    newline()


def play_quiz(all_questions):
    player_score = 0

    for question_no, question in enumerate(all_questions, start=1):
        newline()
        answer: Option | None = None

        while not answer:
            answer = ask_question(question_no, question)

        if answer.is_correct:
            player_score += 1
            show_message(Messages.CORRECT_GUESS.format(option_text=answer.option_text))

        else:
            show_message(Messages.INCORRECT_GUESS.format(option_text=answer.option_text))

        newline()

    return player_score


def play_quiz_screen(player: User, quiz: Quiz):
    newline()
    newline()

    show_message(
        Messages.QUIZ_NAME.format(
            quiz_name=quiz.quiz_name,
            creator_name=quiz.creator_name
        )
    )

    all_questions = get_quiz_questions(quiz)

    if not all_questions:
        show_message(Messages.WORKING_ON_QUIZ)
        explore_quiz_screen(player)
        return

    total_score = len(all_questions)
    player_score = play_quiz(all_questions)

    quiz_record = QuizRecord(
        player.user_id,
        player.username,
        quiz.quiz_id,
        quiz.quiz_name,
        player_score,
        total_score
    )
    add_quiz_record(quiz_record)

    newline()
    show_message(
        OutputTexts.QUIZ_RESULT.format(
            result=(player_score / total_score) * 100,
            quiz_name=quiz.quiz_name
        )
    )


def play_random_quiz(player):
    quiz = get_random_quiz()

    if not quiz:
        newline()
        show_message(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    play_quiz_screen(player, quiz)


def show_player_records(player_records):
    show_message(
        OutputTexts.RECORD_INFO.format(
            record_id=Strings.ID,
            quiz_name=Strings.QUIZ,
            player_name=Strings.PLAYER,
            result=Strings.RESULT,
            played_at=Strings.PLAYED_AT
        )
    )

    for index, quiz in enumerate(player_records, start=1):
        show_record(index, quiz)


def show_player_records_screen(player):
    newline()
    player_records = get_player_records(performer=player)

    if not player_records:
        show_message(OutputTexts.NO_QUIZ_RECORDS)
        return

    show_player_records(player_records)


def select_quiz_screen(all_quizzes, search_key=""):
    newline()

    if not all_quizzes:
        if search_key:
            show_message(OutputTexts.NO_QUIZZES.format(search_key))
        else:
            show_message(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        invalid_choice()
        return

    return selected_quiz


def explore_quiz_screen(player):
    newline()
    search_key = input(InputTexts.KEYWORD)

    all_quizzes = filter_all_quizzes(search_key)
    selected_quiz = select_quiz_screen(all_quizzes, search_key)

    if not selected_quiz:
        return

    play_quiz_screen(player, selected_quiz)
