import sys
import pwinput
import re

from helpers.constants import OutputTexts, InputTexts, Messages, Strings
from data_containers.question import Question
from data_containers.quiz import Quiz
from data_containers.quiz_record import QuizRecord
from data_containers.types import QuizType
from data_containers.user import UserRole, User


def show_user(index, user):
    print(
        OutputTexts.USER_INFO.format(
            user_id=str(index),
            username=user.username,
            user_role=UserRole.to_string(user.role)
        )
    )


def show_type(index, each_type: QuizType):
    print(
        OutputTexts.TYPE_INFO.format(
            type_id=str(index),
            type_name=each_type.type_name
        )
    )


def show_quiz(index, quiz: Quiz):
    print(
        OutputTexts.QUIZ_INFO.format(
            quiz_id=str(index),
            quiz_name=quiz.quiz_name,
            quiz_types=','.join(quiz_type.type_name for quiz_type in quiz.types),
        )
    )


def show_record(index, record: QuizRecord):
    result = (record.player_score / record.total_score) * 100
    print(
        OutputTexts.RECORD_INFO.format(
            record_id=str(index),
            quiz_name=record.quiz_name,
            player_name=record.player_name,
            result=Strings.RESULT_PERCENTAGE.format(result),
            played_at=record.played_at
        )
    )


def show_question(index, question: Question):
    print(
        OutputTexts.QUESTION_INFO.format(
            question_id=str(index),
            question_text=question.question_text
        )
    )


def show_questions_all_info(index, question: Question):
    correct_option = [option for option in question.options if option.is_correct]
    correct_option = correct_option[0]

    print(
        OutputTexts.QUESTION_ALL_INFO.format(
            question_id=str(index),
            question_text=question.question_text,
            option_1=question.options[0].option_text,
            option_2=question.options[1].option_text,
            option_3=question.options[2].option_text,
            option_4=question.options[3].option_text,
            correct_option=correct_option.option_text
        )
    )


def password_input():
    return pwinput.pwinput(InputTexts.PASSWORD)


def quit_application():
    print()
    print("Bye!")
    sys.exit(0)


def greet_user(user: User):
    print()
    print()
    print(Messages.GREET.format(username=user.username))
