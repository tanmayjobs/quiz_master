from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import OkResponse, ErrorSchema, ErrorExamples

blp = Blueprint("Questions", __name__)


@blp.route("/quizzes/<int:quiz_id>/questions")
class QuestionsView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("quiz"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self, quiz_id):
        """
        Add a questions for a quiz.
        """
        ...


@blp.route("/questions/<int:question_id>")
class QuestionView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("question"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def put(self):
        ...

    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("question"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self):
        ...
