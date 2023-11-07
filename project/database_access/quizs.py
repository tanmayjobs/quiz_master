from project.data_containers.user import UserRole
from project.data_containers.quiz import Quiz


def get_by_creator(user) -> list['Quiz']:
    if user.role != UserRole.CREATOR:
        raise PermissionError

    ...  # Get quizzes by creator.


def get_all_quizzes(user) -> list['Quiz']:
    if user.role != UserRole.ADMIN:
        raise PermissionError

    ...  # Get all quizzes.


def add(user, **kwargs) -> None:
    if user.role != UserRole.CREATOR:
        raise PermissionError

    ...  # Add the quiz to database.


def remove(self, user) -> None:
    if self.creator_id != user.user_id and user.role != UserRole.ADMIN:
        raise PermissionError

    ...  # Remove the quiz from the database.
