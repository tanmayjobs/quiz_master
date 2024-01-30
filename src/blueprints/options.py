from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.options.add_option import AddOptionController
from controllers.options.remove_option import RemoveOptionController
from controllers.options.update_option import UpdateOptionController
from helpers.constants import Strings
from helpers.constants.http_statuses import AUTHORIZATION_HEADER
from schemas import OkResponse, ErrorResponse, ErrorExamples, OptionRequest

blp = Blueprint("Options", __name__)


@blp.route("/questions/<string:question_id>/options")
class OptionsView(MethodView):
    @blp.arguments(OptionRequest)
    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404(Strings.QUESTION)
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def post(self, json_data, question_id):
        add_option = AddOptionController(question_id, json_data)
        return add_option()


@blp.route("/options/<string:option_id>")
class OptionView(MethodView):
    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404(Strings.OPTION)
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def delete(self, option_id):
        remove_option = RemoveOptionController(option_id)
        return remove_option()

    @blp.arguments(OptionRequest)
    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404(Strings.OPTION)
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def put(self, json_data, option_id):
        update_controller = UpdateOptionController(option_id, json_data)
        return update_controller()
