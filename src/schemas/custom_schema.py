import typing

from marshmallow import Schema, ValidationError
from helpers.exceptions import ValidationCustomException


class CustomSchema(Schema):
    def handle_error(
        self, error: ValidationError, data: typing.Any, *, many: bool, **kwargs
    ):
        raise ValidationCustomException(error)
