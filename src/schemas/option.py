from marshmallow.fields import String, Boolean

from .custom_schema import CustomSchema


class OptionRequest(CustomSchema):
    option_text = String(required=True)
    is_correct = Boolean(required=True)


class OptionResponse(CustomSchema):
    id = String(required=True)
    option_text = String(required=True)
    is_correct = Boolean()
