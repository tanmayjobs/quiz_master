from constants import Errors
from data_containers.user import UserRole


def admin_only(func):
    def secured_function(*args, **kwargs):
        performer = kwargs.get("performer")

        if not performer:
            raise ValueError(Errors.PERFORMER_REQUIRED)

        if performer.role != UserRole.ADMIN:
            raise PermissionError(Errors.PERMISSION)

        return func(*args, **kwargs)

    return secured_function
