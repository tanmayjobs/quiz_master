from constants import InputTexts, OutputTexts, Errors, Messages
from controller.user import add_creator
from helpers.common import show_message
from helpers.common import newline, password_input


def add_creator_screen(user):
    newline()
    show_message(Messages.CREATOR_INFO)

    username, password = input(InputTexts.USERNAME), password_input()
    is_user_added = add_creator(username, password, performer=user)

    if is_user_added:
        show_message(OutputTexts.CREATOR_ADDED)
    else:
        show_message(Errors.USERNAME_ALREADY_EXISTS)

