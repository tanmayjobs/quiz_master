from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import OkResponse, ErrorResponse, ErrorExamples

blp = Blueprint("Questions", __name__)


@blp.route("/quizzes/<int:quiz_id>/questions")
class QuestionsView(MethodView):
    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("quiz"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self, quiz_id):
        """
        Add a questions for a quiz.
        """
        ...


@blp.route("/questions/<int:question_id>")
class QuestionView(MethodView):
    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("question"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def put(self):
        ...

    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("question"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self):
        ...
