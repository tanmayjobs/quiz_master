from dataclasses import dataclass

from helpers.constants import Errors, LogText
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

    def __repr__(self):
        return f"{self.code}, {self.error}, {self.message}"


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
    def __init__(self, message):
        super().__init__(
            HTTPStatuses.CONFLICT.code, HTTPStatuses.CONFLICT.status, message
        )


class DoNotExists(CustomException):
    def __init__(self, message):
        super().__init__(
            HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, message
        )


class NotEnoughPermission(CustomException):
    def __init__(self):
        super().__init__(
            HTTPStatuses.FORBIDDEN.code,
            HTTPStatuses.FORBIDDEN.status,
            Errors.NOT_ENOUGH_PERMISSIONS,
        )


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
            Errors.TOKEN_NOT_FRESH,
        )


class BlockedToken(CustomException):
    def __init__(self):
        super().__init__(
            HTTPStatuses.INVALID_TOKEN.code,
            HTTPStatuses.INVALID_TOKEN.status,
            Errors.BLOCKED_TOKEN,
        )


class TokenNotProvided(CustomException):
    def __init__(self):
        super().__init__(
            HTTPStatuses.UNAUTHORIZED.code,
            HTTPStatuses.UNAUTHORIZED.status,
            Errors.TOKEN_NOT_PROVIDED,
        )


class TokenExpired(CustomException):
    def __init__(self):
        super().__init__(
            HTTPStatuses.INVALID_TOKEN.code,
            HTTPStatuses.INVALID_TOKEN.status,
            Errors.EXPIRED_TOKEN,
        )


class InvalidQuizResponse(CustomException):
    def __init__(self, message, hints):
        self.hints = hints
        super().__init__(
            HTTPStatuses.BAD_REQUEST.code,
            HTTPStatuses.BAD_REQUEST.status,
            message
        )

    def dump(self):
        return {**super().dump(), "hints": self.hints}


def register_error_handlers(app):
    app.logger.info(LogText.REGISTER_ERROR_HANDLERS)
    app.register_error_handler(NotEnoughPermission, lambda err: err.generate_response())
    app.register_error_handler(BlockedToken, lambda err: err.generate_response())
    app.register_error_handler(ValidationCustomException, lambda err: err.generate_response())
    app.logger.info(LogText.REGISTER_ERROR_HANDLERS_COMPLETED)