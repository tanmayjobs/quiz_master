from controller.user import get_all_users
from helpers.common import new_line


def remove_user_screen(user):
    new_line()
    all_users = get_all_users(performer=user)
    ...  # show all users
