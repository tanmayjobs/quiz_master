import services.users as user_services
from helpers.rbac import admin_only
from data_containers.user import *
from helpers.crypt import check_password


def sign_in(username, password) -> User | None:
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


@admin_only
def add_creator(username, password, **kwargs) -> bool:
    is_user_added = user_services.add_user(username, password, UserRole.CREATOR)
    return is_user_added


@admin_only
def get_all_users(**kwargs) -> list[User]:
    all_user_data = user_services.get_all_users()
    all_users = [User.parse_database(user_data) for user_data in all_user_data]

    return all_users


@admin_only
def remove_user(user, **kwargs) -> None:
    user_services.remove_user(user.user_id)
