import services.user as user_services

from utils.rbac import accessed_by
from data_containers.user import *


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
