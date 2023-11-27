import sqlite3
from unittest.mock import Mock, MagicMock, patch

import pytest

from data_containers.last_transaction import LastTransaction
from data_containers.question import Question
from data_containers.user import User, UserRole
from database import DBContext
from src.handler.questions import QuestionHandler

questions_data = [
    (
        1,
        "who is the batman?",
        '{"option":"bruce wayne","is_correct":1},{"option":"alfred","is_correct":0},{"option":"joker","is_correct":0},{"option":"edward nigma","is_correct":0}',
    ),
    (
        2,
        "who killed the batman?",
        '{"option":"the riddler","is_correct":0},{"option":"joker","is_correct":0},{"option":"batman who laughs","is_correct":1},{"option":"obito","is_correct":0}',
    ),
]


@pytest.fixture()
def mock_db_context():
    mock_db_ctx = MagicMock(spec=DBContext)
    mock_db_ctx.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_ctx.return_value = mock_db_ctx
    mock_db_ctx.__enter__.return_value = mock_db_ctx
    return mock_db_ctx


@pytest.fixture()
def mock_user():
    mocked_user = Mock(spec=User)
    mocked_user.username = "batman"
    mocked_user.role = UserRole.CREATOR
    return mocked_user


@pytest.fixture()
def mock_question():
    mocked_question = Mock(spec=Question)
    mocked_question.question_text = "Question"
    mocked_question.options = []
    return mocked_question


def test_add_question(mock_user, mock_question, mock_db_context):
    with patch("src.handler.questions.DBContext", mock_db_context):
        mock_last_transaction = MagicMock(spec=LastTransaction)
        mock_last_transaction.rows_changed = 1
        mock_last_transaction.last_id = 1
        mock_db_context.write.return_value = mock_last_transaction
        QuestionHandler(1, mock_user).add_question(mock_question)


def test_get_quiz_question(mock_db_context):
    with patch("src.handler.questions.DBContext", mock_db_context):
        mock_db_context.read.return_value = questions_data
        expected = [
            Question.parse_json(question_data) for question_data in questions_data
        ]
        assert expected == QuestionHandler(1).get_quiz_questions()


def test_remove_question(mock_user, mock_db_context):
    with patch("src.handler.questions.DBContext", mock_db_context):
        mock_db_context.write = Mock()
        mock_db_context.write.return_value = True
        QuestionHandler(1, mock_user).remove_question(1)
