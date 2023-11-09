from service.users import get_by_username, add_user
from data_containers.user import *
from helpers.crypt import check_password


def sign_in(username, password) -> User | None:
    user = get_by_username(username)

    if not user or check_password(password, user.password_hash):
        return None

    return user


def sign_up(username, password, role=UserRole.PLAYER) -> bool:
    is_user_added = add_user(username, password, role)
    return is_user_added
