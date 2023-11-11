from constants import SQLQueries
from data_containers.user import UserRole, User
from database.operations import *
from sqlite3 import IntegrityError
from helpers.crypt import hash_password


def get_all_users() -> list['User']:
    data = get(SQLQueries.GET_ALL_USERS, None)
    return data


def add_user(username: str, password: str, role: UserRole) -> bool:
    password_hash = hash_password(password)
    try:
        add(SQLQueries.ADD_USER, (username, password_hash, role))

    except IntegrityError:
        return False

    return True


def remove_user(user: User) -> None:
    remove(SQLQueries.REMOVE_USER, (user.user_id, ))


def get_by_username(username: str):
    result = get(SQLQueries.GET_USER, (username, ), True)
    return result
