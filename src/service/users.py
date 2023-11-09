from src.data_containers.user import UserRole, User


def get_all_users() -> list['User']:
    return []  # Return the list of users.


def add_user(username, password, role) -> bool:  # Here kwargs include username, password, role.
    ...  # Add the user in database.
    return True


def remove_user(user: User) -> None:
    ...  # Remove the user from the database.


def get_by_username(username: str) -> 'User' | None:
    return  # Get user using username.
