from project.data_containers.user import *


def sign_in():
    username, password = ...
    user: User | None = User.get(username, password)
    return user


def sign_up() -> bool:
    username, password = ...
    User.add(username, password)
