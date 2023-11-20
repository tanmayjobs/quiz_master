from constants import OutputTexts, InputTexts, Strings
from controller.user import get_all_users, remove_user
from screens.common import newline, show_message, show_user, invalid_choice


def show_all_users(all_users):
    show_message(
        OutputTexts.USER_INFO.format(
            user_id=Strings.ID,
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
    newline()

    all_users = get_all_users(performer=user)

    if not all_users:
        show_message(OutputTexts.NOT_YET.format(Strings.USER))
        return

    show_all_users(all_users)

    user_for_removal = select_user(all_users)

    if not user_for_removal:
        invalid_choice()
        return

    remove_user(user_for_removal, performer=user)
    show_message(OutputTexts.USER_REMOVED)
