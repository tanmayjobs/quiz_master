import sys
import pwinput

from constants import OutputTexts, InputTexts, Strings
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


def password_input():
    return pwinput.pwinput(InputTexts.PASSWORD)


def newline():
    print()


def quit_application():
    newline()
    print("Bye!")
    sys.exit(0)
