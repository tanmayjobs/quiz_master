import sys
import pwinput

from constants import OutputTexts, InputTexts
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


def password_input():
    return pwinput.pwinput(InputTexts.PASSWORD)


def new_line():
    print()


def quit_application():
    new_line()
    print("Bye!")
    sys.exit(0)
