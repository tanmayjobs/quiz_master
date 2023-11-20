import services.user as user_services

from data_containers.user import *
from utils.crypt import check_password


def sign_in(username, password) -> User | None:

    if not username.strip() or not password:
        return None

    user_data = user_services.get_by_username(username)

    if not user_data:
        return None

    user = User.parse_database(user_data)

    if not check_password(password, user.password_hash):
        return None

    return user


def sign_up(username, password) -> bool:

    if not username.strip() or not password:
        return False

    is_user_added = user_services.add_user(username, password, UserRole.PLAYER)
    return is_user_added
