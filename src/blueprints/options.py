from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import OkResponse,  ErrorResponse, ErrorExamples

blp = Blueprint("Options", __name__)


@blp.route("/questions/<int:question_id>/options")
class OptionsView(MethodView):
    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("question"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[
        {'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self):
        ...


@blp.route("/options/<int:option_id>")
class OptionView(MethodView):
    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("options"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self):
        ...

    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("options"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def put(self):
        ...
