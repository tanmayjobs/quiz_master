from controller.user import UserHandler
from helpers.constants import OutputTexts, InputTexts, Strings
from screens.common import show_user


def show_all_users(all_users):
    print(
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
    print()

    user_handler = UserHandler(user)
    all_users = user_handler.get_all_users()

    if not all_users:
        print(OutputTexts.NOT_YET.format(Strings.USER))
        return

    show_all_users(all_users)

    user_for_removal = select_user(all_users)

    if not user_for_removal:
        print(OutputTexts.INVALID_CHOICE)
        return

    user_handler.remove_user(user_for_removal, performer=user)
    print(OutputTexts.USER_REMOVED)
