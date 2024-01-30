from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.questions.add_question import AddQuestionController
from controllers.questions.get_question import GetQuestionController
from controllers.questions.get_questions import GetQuestionsController
from controllers.questions.remove_question import RemoveQuestionController
from controllers.questions.update_question import UpdateQuestionController
from helpers.constants.http_statuses import AUTHORIZATION_HEADER
from schemas import (
    QuestionRequest,
    OkResponse,
    ErrorResponse,
    ErrorExamples,
    UpdateQuestionRequest,
    QuestionResponse,
    QuestionsResponse,
)

blp = Blueprint("Questions", __name__)


@blp.route("/quizzes/<string:quiz_id>/questions")
class QuestionsView(MethodView):
    @blp.alt_response(200, schema=QuestionsResponse)
    def get(self, quiz_id):
        get_questions = GetQuestionsController(quiz_id)
        return get_questions()

    @blp.arguments(QuestionRequest)
    @blp.alt_response(404, schema=ErrorResponse, example=ErrorExamples.error404("quiz"))
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def post(self, json_data, quiz_id):
        add_question = AddQuestionController(quiz_id, json_data)
        return add_question()


@blp.route("/questions/<string:question_id>")
class QuestionView(MethodView):
    @blp.alt_response(200, schema=QuestionResponse)
    def get(self, question_id):
        get_question = GetQuestionController(question_id)
        return get_question()

    @blp.arguments(UpdateQuestionRequest)
    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404("question")
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def put(self, json_data, question_id):
        update_question = UpdateQuestionController(question_id, json_data)
        return update_question()

    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404("question")
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def delete(self, question_id):
        remove_question = RemoveQuestionController(question_id)
        return remove_question()
