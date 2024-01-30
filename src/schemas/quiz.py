from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema
from marshmallow.fields import String, List, Nested, validate

from .tags import TagResponse


class QuizRequest(CustomSchema):
    quiz_name = String(required=True, validate=validate.Regexp(RegexPatterns.ALPHA_NUM_Q2))
    tag_ids = List(String, validate=validate.Length(min=1))


class QuizResponse(CustomSchema):
    creator_id = String(required=True)
    creator_name = String(required=True)
    quiz_id = String(required=True, dump_only=True)
    quiz_name = String(required=True, dump_only=True)
    tags = List(Nested(TagResponse()), required=True)


class QuizzesResponse(CustomSchema):
    quizzes = List(Nested(QuizResponse()), required=True)


class RecordFilter(CustomSchema):
    quiz_id = String()
    user_id = String()


class Records(CustomSchema):
    records = List(Nested(RecordFilter()), dump_only=True)


class Answer(CustomSchema):
    question_id = String(required=True)
    selected_option_ids = List(String, required=True, validate=validate.Length(min=1))


class CreateRecord(CustomSchema):
    quiz_id = String(required=True)
    answers = List(Nested(Answer()), required=True)
