from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema
from marshmallow.fields import String, List, Nested, validate


class AddTagRequest(CustomSchema):
    tag_name = String(required=True, validate=validate.Regexp(RegexPatterns.ALPHA_NUM_Q2))


class TagResponse(CustomSchema):
    tag_id = String(required=True, dump_only=True)
    tag_name = String(required=True, dump_only=True)


class TagsResponse(CustomSchema):
    tags = List(Nested(TagResponse()), required=True)
