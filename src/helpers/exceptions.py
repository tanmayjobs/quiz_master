import json
from dataclasses import dataclass

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


class ValidationException(CustomException):
    ...


class InvalidCredentials(CustomException):
    ...


class AlreadyExists(CustomException):
    ...


class DoNotExists(CustomException):
    def __init__(self, message, code=HTTPStatuses.NOT_FOUND.code, status=HTTPStatuses.NOT_FOUND.status):
        super().__init__(code, status, message)


class NotEnoughPermission(CustomException):
    ...


class ValidationCustomException(CustomException):
    def __init__(self, error):
        self.hints = error.messages
        super().__init__(
            HTTPStatuses.UNPROCCESSABLE_ENTITY.code,
            HTTPStatuses.UNPROCCESSABLE_ENTITY.status,
            HTTPStatuses.UNPROCCESSABLE_ENTITY.status
        )

    def dump(self):
        return {**super().dump(), "hints": self.hints}
