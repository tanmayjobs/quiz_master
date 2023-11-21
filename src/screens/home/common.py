from controller.questions import QuestionHandler
from controller.quiz import QuizHandler
from controller.quiz_record import QuizRecordHandler
from helpers.constants import OutputTexts, Strings, InputTexts, Messages, Numbers

from data_containers.question import Option
from data_containers.quiz import Quiz
from data_containers.quiz_record import QuizRecord
from data_containers.user import User

from screens.common import show_quiz, show_record


def show_all_quizzes(all_quizzes):
    print(
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


def select_creator_quiz_screen(user):
    print()
    all_quizzes = QuizHandler(user).get_user_quizzes()

    if not all_quizzes:
        print(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        print(OutputTexts.INVALID_CHOICE)
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
            print(OutputTexts.INVALID_CHOICE)

    else:
        print(OutputTexts.INVALID_CHOICE)

    print()


def play_quiz(all_questions):
    player_score = 0

    for question_no, question in enumerate(all_questions, start=1):
        print()
        answer: Option | None = None
        correct_option = [option for option in question.options if option.is_correct][0]

        while not answer:
            answer = ask_question(question_no, question)

        if answer.is_correct:
            player_score += 1
            print(Messages.CORRECT_GUESS.format(option_text=answer.option_text))

        else:
            print(Messages.INCORRECT_GUESS.format(option_text=correct_option.option_text))

        print()

    return player_score


def show_quiz_result(quiz_record: QuizRecord):
    print()
    print(
        OutputTexts.QUIZ_RESULT.format(
            result=(quiz_record.player_score / quiz_record.total_score) * 100,
            quiz_name=quiz_record.quiz_name
        )
    )

    print()

    top_records = QuizRecordHandler.quiz_top_records(quiz_record.quiz_id)

    if top_records:
        print(Messages.TOP_RECORD)
        show_records_screen(top_records)
        print()


def play_quiz_screen(player: User, quiz: Quiz):
    print()
    print()

    print(
        Messages.QUIZ_NAME.format(
            quiz_name=quiz.quiz_name,
            creator_name=quiz.creator_name
        )
    )

    all_questions = QuestionHandler(quiz.quiz_id).get_quiz_questions()

    if not all_questions:
        print(Messages.WORKING_ON_QUIZ)
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

    QuizRecordHandler.add_quiz_record(quiz_record)
    show_quiz_result(quiz_record)


def play_random_quiz(player):
    quiz = QuizHandler.get_random_quiz()

    if not quiz:
        print()
        print(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    play_quiz_screen(player, quiz)


def show_records_screen(player_records):
    print(
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


def show_player_records_screen(user):
    print()
    player_records = QuizRecordHandler.get_user_records(user)

    if not player_records:
        print(OutputTexts.NO_QUIZ_RECORDS)
        return

    show_records_screen(player_records)


def select_quiz_screen(all_quizzes, search_key=""):
    print()

    if not all_quizzes:
        if search_key:
            print(OutputTexts.NO_QUIZZES.format(search_key))
        else:
            print(OutputTexts.NOT_YET.format(Strings.QUIZ))
        return

    show_all_quizzes(all_quizzes)

    selected_quiz = select_quiz(all_quizzes)

    if not selected_quiz:
        print(OutputTexts.INVALID_CHOICE)
        return

    return selected_quiz


def explore_quiz_screen(player):
    print()
    search_key = input(InputTexts.KEYWORD)

    all_quizzes = QuizHandler.filter_all_quizzes(search_key)
    selected_quiz = select_quiz_screen(all_quizzes, search_key)

    if not selected_quiz:
        return

    play_quiz_screen(player, selected_quiz)
