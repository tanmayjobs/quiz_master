from helpers.constants import Strings
from enum import Enum


class UserRole(Enum):
    ADMIN = 0
    CREATOR = 1
    PLAYER = 2

    @staticmethod
    def to_string(role_val):
        match role_val:
            case UserRole.ADMIN:
                return Strings.ADMIN
            case UserRole.CREATOR:
                return Strings.CREATOR
            case UserRole.PLAYER:
                return Strings.PLAYER
            case other:
                raise ValueError
