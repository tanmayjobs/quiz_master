from constants import Errors, Strings
from data_containers.user import UserRole


def admin_only(func):
    def secured_function(*args, **kwargs):
        performer = kwargs.get(Strings.PERFORMER)

        if not performer:
            raise ValueError(Errors.PERFORMER_REQUIRED)

        if performer.role != UserRole.ADMIN:
            raise PermissionError(Errors.PERMISSION)

        return func(*args, **kwargs)

    return secured_function


def creator_only(func):
    def secured_function(*args, **kwargs):
        performer = kwargs.get(Strings.PERFORMER)

        if not performer:
            raise ValueError(Errors.PERFORMER_REQUIRED)

        if performer.role != UserRole.CREATOR:
            raise PermissionError(Errors.PERMISSION)

        return func(*args, **kwargs)

    return secured_function
