import sys
import pwinput

from constants import OutputTexts, InputTexts, Strings
from data_containers.question import Question
from data_containers.quiz import Quiz
from data_containers.quiz_record import QuizRecord
from data_containers.types import QuizType
from data_containers.user import UserRole


def invalid_choice():
    print(OutputTexts.INVALID_CHOICE)


def show_message(msg):
    print(msg)


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
            type_id=str(each_type.type_id),
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
            result=str(float("{0:.2f}".format(result))),
        )
    )


def show_question(index, question: Question):
    print(
        OutputTexts.QUESTION_INFO.format(
            question_id=str(index),
            question_text=question.question_text
        )
    )


def password_input():
    return pwinput.pwinput(InputTexts.PASSWORD)


def newline():
    print()


def quit_application():
    newline()
    print("Bye!")
    sys.exit(0)
