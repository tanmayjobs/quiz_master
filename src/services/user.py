from database import database

from constants import SQLQueries
from data_containers.user import UserRole
from sqlite3 import IntegrityError
from utils.crypt import hash_password


def get_all_users() -> list:
    data = database.get(SQLQueries.GET_ALL_USERS)
    return data


def add_user(username: str, password: str, role: UserRole) -> bool:
    password_hash = hash_password(password)

    try:
        database.add(SQLQueries.ADD_USER, (username, password_hash, role))

    except IntegrityError:
        return False

    return True


def remove_user(user_id: str) -> None:
    database.remove(SQLQueries.REMOVE_USER, (user_id,))


def get_by_username(username: str):
    result = database.get(SQLQueries.GET_USER, (username,), True)
    return result
