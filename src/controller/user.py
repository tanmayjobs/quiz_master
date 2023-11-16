import services.user as user_services

from helpers.rbac import accessed_by
from data_containers.user import *
from helpers.crypt import check_password


def sign_in(username, password) -> User | None:

    if not username.strip() or not password:
        raise ValueError

    user_data = user_services.get_by_username(username)

    if not user_data:
        return None

    user = User.parse_database(user_data)

    if not check_password(password, user.password_hash):
        return None

    return user


def sign_up(username, password) -> bool:
    is_user_added = user_services.add_user(username, password, UserRole.PLAYER)
    return is_user_added


@accessed_by(UserRole.ADMIN)
def add_creator(username, password, **_) -> bool:
    is_user_added = user_services.add_user(username, password, UserRole.CREATOR)
    return is_user_added


@accessed_by(UserRole.ADMIN)
def get_all_users(**_) -> list[User]:
    all_user_data = user_services.get_all_users()
    all_users = [User.parse_database(user_data) for user_data in all_user_data]

    return all_users


@accessed_by(UserRole.ADMIN)
def remove_user(user, **_) -> None:
    user_services.remove_user(user.user_id)
