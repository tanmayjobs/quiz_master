from project.data_containers.user import UserRole, User


def get_all_users(user) -> list['User']:
    if user.role != UserRole.ADMIN:
        raise PermissionError

    return []  # Return the list of users.


def add(username, password, role) -> None:  # Here kwargs include username, password, role.
    ...  # Add the user in database.


def remove(self) -> None:
    ...  # Remove the user from the database.


def get_by_username(username: str) -> 'User' | None:
    return  # Get user using username.
