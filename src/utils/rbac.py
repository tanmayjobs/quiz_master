from data_containers.user import UserRole, User
from helpers.constants import Errors


def accessed_by(*roles: tuple[UserRole]):
    """
    accessed_by is used as a decorator to apply rbac on any methods.
    :param roles: requires the User Roles which can access any function.
    :return: returns the secured function.

    Example:
        ...
        from utils.rbac import accessed_by

        class Handler:
            def __init__(self, user):
                self.user = user

            @accessed_by(UserRole.ADMIN, UserRole.CREATOR)
            def remove_quiz(quiz):
                with DBContext(database) as dao:
                    ...

        accessed_by decorator is applied on a instance method of a class and the class must have a defined user instance.

    """

    def wrapper(func):
        def secured_function(self, *args, **kwargs):
            """
            This function add the secured functionality check on any instance method of a class.
            By checking the user and it's role.
            :param self: You know what it is.
            :param args: Again you know.
            :param kwargs: Again you know.
            :return: Returns the decorated secured function.
            """

            # TODO: Here rather than taking the user object it will be better to use user_id and check the role in db
            # TODO: Here rather than raising error we will send suitable response

            if not isinstance(self.user, User):
                raise ValueError(Errors.PERFORMER_REQUIRED)
            if self.user.role not in roles:
                raise PermissionError(Errors.PERMISSION)

            return func(self, *args, **kwargs)

        return secured_function

    return wrapper
