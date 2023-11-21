from controller.user import UserHandler
from data_containers.user import UserRole
from helpers.constants import InputTexts, OutputTexts, Errors, Messages
from screens.common import validate_password
from screens.common import password_input


def add_creator_screen(user):
    print()
    print(Messages.CREATOR_INFO)

    username, password = input(InputTexts.USERNAME), password_input()

    if not username:
        print(Errors.USERNAME_EMPTY)
        return

    if not validate_password(password):
        print(Errors.WEAK_PASSWORD)
        return

    is_user_added = UserHandler(user).add_user(username, password)

    if is_user_added:
        print(OutputTexts.CREATOR_ADDED)
    else:
        print(Errors.USERNAME_ALREADY_EXISTS)
