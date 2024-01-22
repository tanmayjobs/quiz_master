from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import OkResponse,  ErrorSchema, ErrorExamples

blp = Blueprint("Options", __name__)


@blp.route("/questions/<int:question_id>/options")
class OptionsView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("question"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[
        {'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self):
        ...


@blp.route("/options/<int:option_id>")
class OptionView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("options"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self):
        ...

    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("options"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def put(self):
        ...
