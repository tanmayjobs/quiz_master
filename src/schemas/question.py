from .custom_schema import CustomSchema
from marshmallow.fields import String, List, Nested, validate

from .option import OptionRequest


class QuestionRequest(CustomSchema):
    question_text = String(required=True)
    options = List(Nested(OptionRequest()), validate=validate.Length(min=2, max=5))


class UpdateQuestionRequest(CustomSchema):
    question_text = String(required=True)
