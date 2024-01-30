from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.tags.create_tag import CreateTagController
from controllers.tags.get_tags import GetTagsController
from helpers.constants.http_statuses import HTTPStatuses, AUTHORIZATION_HEADER
from schemas import AddTagRequest, OkResponse, TagsResponse

blp = Blueprint("Tags", __name__)


@blp.route("/tags")
class TagsView(MethodView):
    @blp.alt_response(HTTPStatuses.OK.code, schema=TagsResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        get_tags = GetTagsController()
        return get_tags()

    @blp.arguments(AddTagRequest)
    @blp.alt_response(HTTPStatuses.CREATED.code, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def post(self, json_data):
        create_tag = CreateTagController(json_data)
        return create_tag()
