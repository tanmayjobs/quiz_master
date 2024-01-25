from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema
from marshmallow.fields import String, List, Nested, validate

from .tags import TagResponse


class QuizRequest(CustomSchema):
    quiz_name = String(required=True)
    tag_ids = List(String, validate=validate.Length(min=1))


class QuizResponse(CustomSchema):
    creator_id = String(required=True)
    creator_name = String(required=True)
    quiz_id = String(required=True, dump_only=True)
    quiz_name = String(required=True, dump_only=True)
    tags = List(Nested(TagResponse()), required=True)


class QuizzesResponse(CustomSchema):
    quizzes = List(Nested(QuizResponse()), required=True)
