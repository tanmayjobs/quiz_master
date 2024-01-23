from dataclasses import dataclass


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


class DBException(CustomException):
    ...


class ValidationException(CustomException):
    ...


class InvalidCredentials(CustomException):
    ...


class AlreadyExists(CustomException):
    ...


class DoNotExists(CustomException):
    ...


class NotEnoughPermission(CustomException):
    ...
