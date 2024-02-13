from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.tags.create_tag import CreateTagController
from controllers.tags.delete_tag import DeleteTagController
from controllers.tags.get_tags import GetTagsController
from controllers.tags.update_tag import UpdateTagController
from helpers.constants.http_statuses import HTTPStatuses, AUTHORIZATION_HEADER
from schemas import TagRequest, OkResponse, TagsResponse

blp = Blueprint("Tags", __name__)


@blp.route("/tags")
class TagsView(MethodView):
    @blp.alt_response(HTTPStatuses.OK.code, schema=TagsResponse)
    def get(self):
        get_tags = GetTagsController()
        return get_tags()

    @blp.arguments(TagRequest)
    @blp.alt_response(HTTPStatuses.CREATED.code, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def post(self, json_data):
        create_tag = CreateTagController(json_data)
        return create_tag()


@blp.route("/tags/<string:tag_id>")
class TagView(MethodView):
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def delete(self, tag_id):
        delete_tag = DeleteTagController(tag_id)
        return delete_tag()

    @blp.arguments(TagRequest)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def put(self, json_data, tag_id):
        update_tag = UpdateTagController(tag_id, json_data)
        return update_tag()
