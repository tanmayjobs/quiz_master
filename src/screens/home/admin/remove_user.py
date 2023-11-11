from constants import OutputTexts, InputTexts, Strings
from controller.user import get_all_users, remove_user
from helpers.common import new_line, show_message, show_user, invalid_choice


def show_all_users(all_users):
    show_message(
        OutputTexts.USER_INFO.format(
            user_id=Strings.USER_ID,
            username=Strings.USERNAME,
            user_role=Strings.ROLE
        )
    )

    for index, user in enumerate(all_users, start=1):
        show_user(index, user)


def select_user(all_users):
    index = input(InputTexts.USER_ID)

    if not index.isdigit():
        return None

    index = int(index) - 1

    if index < 0 or index > len(all_users) - 1:
        return None

    return all_users[index]


def remove_user_screen(user):
    new_line()

    all_users = get_all_users(performer=user)
    show_all_users(all_users)

    user_for_removal = select_user(all_users)

    if not user_for_removal:
        invalid_choice()
        return

    remove_user(user_for_removal, performer=user)
    show_message(OutputTexts.USER_REMOVED)
