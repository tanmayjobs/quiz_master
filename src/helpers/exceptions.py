import json
from dataclasses import dataclass

from helpers.constants import Errors
from helpers.constants.http_statuses import HTTPStatuses


@dataclass
class CustomException(Exception):
    code: int
    error: str
    message: str

    def dump(self):
        return {
            "code": self.code,
            "error": self.error,
            "message": self.message,
        }

    def generate_response(self):
        return self.dump(), self.code


class ValidationException(CustomException):
    ...


class InvalidCredentials(CustomException):
    def __init__(
            self,
            message,
            code=HTTPStatuses.UNAUTHORIZED.code,
            status=HTTPStatuses.UNAUTHORIZED.status,
    ):
        super().__init__(code, status, message)


class AlreadyExists(CustomException):
    def __init__(
            self,
            message,
            code=HTTPStatuses.CONFLICT.code,
            status=HTTPStatuses.CONFLICT.status,
    ):
        super().__init__(code, status, message)


class DoNotExists(CustomException):
    def __init__(
            self,
            message,
            code=HTTPStatuses.NOT_FOUND.code,
            status=HTTPStatuses.NOT_FOUND.status,
    ):
        super().__init__(code, status, message)


class NotEnoughPermission(CustomException):
    def __init__(
            self,
            message=Errors.NOT_ENOUGH_PERMISSIONS,
            code=HTTPStatuses.FORBIDDEN.code,
            status=HTTPStatuses.FORBIDDEN.status,
    ):
        super().__init__(code, status, message)


class ValidationCustomException(CustomException):
    def __init__(self, error):
        self.hints = error.messages
        super().__init__(
            HTTPStatuses.UNPROCCESSABLE_ENTITY.code,
            HTTPStatuses.UNPROCCESSABLE_ENTITY.status,
            HTTPStatuses.UNPROCCESSABLE_ENTITY.status,
        )

    def dump(self):
        return {**super().dump(), "hints": self.hints}


class TokenNotFresh(CustomException):
    def __init__(self):
        super().__init__(
            HTTPStatuses.INVALID_TOKEN.code,
            HTTPStatuses.INVALID_TOKEN.status,
            Errors.TOKEN_NOT_FRESH
        )


class BlockedToken(CustomException):
    def __init__(self):
        super().__init__(HTTPStatuses.INVALID_TOKEN.code, HTTPStatuses.INVALID_TOKEN.status, Errors.BLOCKED_TOKEN)
