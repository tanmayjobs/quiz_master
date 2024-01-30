from .custom_schema import CustomSchema
from marshmallow.fields import String, List, Nested, validate

from .option import OptionRequest, OptionResponse


class QuestionRequest(CustomSchema):
    question_text = String(required=True)
    options = List(
        Nested(OptionRequest()), required=True, validate=validate.Length(min=2, max=5)
    )


class UpdateQuestionRequest(CustomSchema):
    question_text = String(required=True)


class QuestionResponse(CustomSchema):
    question_id = String(required=True)
    question_text = String(required=True)
    options = List(Nested(OptionResponse()), required=True)


class QuestionsResponse(CustomSchema):
    questions = List(Nested(QuestionResponse()), required=True)
