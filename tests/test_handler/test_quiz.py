import sqlite3
from unittest.mock import Mock, MagicMock, patch

import pytest
from pytest import raises

from data_containers.last_transaction import LastTransaction
from data_containers.quiz import Quiz
from data_containers.user import User, UserRole
from database import DBContext
from src.handler.quiz import QuizHandler


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
def mock_quiz():
    mocked_quiz = Mock(spec=Quiz)
    mocked_quiz.quiz_id = 1
    mocked_quiz.quiz_name = ""
    mocked_quiz.creator_id = ""
    mocked_quiz.types = ""
    return mocked_quiz


def test_add_quiz_negative(mock_user):
    with raises(ValueError):
        QuizHandler(mock_user).add_quiz()


def test_add_quiz_positive(mock_user, mock_quiz, mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_last_transaction = MagicMock(spec=LastTransaction)
        mock_last_transaction.rows_changed = 1
        mock_last_transaction.last_id = 1
        mock_db_context.write.return_value = mock_last_transaction
        QuizHandler(mock_user, mock_quiz).add_quiz()


def test_get_random_quiz_negative(mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.read.return_value = None
        expected_value = None
        assert expected_value == QuizHandler.get_random_quiz()


def test_get_random_quiz_positive(mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        quiz_data = (
            1,
            "Quiz Name",
            1,
            "Creator Name",
            '{"type_id":1,"type_name":"Movie"}',
        )
        mock_db_context.read.return_value = quiz_data
        expected_value = Quiz.parse_json(quiz_data)
        assert expected_value == QuizHandler.get_random_quiz()


@pytest.mark.parametrize(
    "quizzes_data",
    [
        tuple(),
        ((1, "Quiz Name", 1, "Creator Name", '{"type_id":1,' '"type_name":"Movie"}'),),
    ],
)
def test_get_user_quizzes(quizzes_data, mock_user, mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.read.return_value = quizzes_data
        expected_value = [Quiz.parse_json(quiz_data) for quiz_data in quizzes_data]
        assert expected_value == QuizHandler(mock_user).get_user_quizzes()


@pytest.mark.parametrize(
    "quizzes_data",
    [
        tuple(),
        ((1, "Quiz Name", 1, "Creator Name", '{"type_id":1,' '"type_name":"Movie"}'),),
    ],
)
def test_get_all_quizzes(quizzes_data, mock_user, mock_db_context):
    mock_user.role = UserRole.ADMIN
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.read.return_value = quizzes_data
        expected_value = [Quiz.parse_json(quiz_data) for quiz_data in quizzes_data]
        assert expected_value == QuizHandler(mock_user).get_all_quizzes()


@pytest.mark.parametrize(
    "quizzes_data",
    [
        tuple(),
        ((1, "Quiz Name", 1, "Creator Name", '{"type_id":1,' '"type_name":"Movie"}'),),
    ],
)
def test_filter_all_quizzes(quizzes_data, mock_user, mock_db_context):
    mock_user.role = UserRole.ADMIN
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.read.return_value = quizzes_data
        expected_value = [Quiz.parse_json(quiz_data) for quiz_data in quizzes_data]
        assert expected_value == QuizHandler(mock_user).filter_all_quizzes("")


def test_remove_quiz_negative(mock_user, mock_db_context):
    with raises(ValueError):
        with patch("src.handler.quiz.DBContext", mock_db_context):
            mock_db_context.write.return_value = False
            QuizHandler(mock_user).remove_quiz()


def test_remove_quiz_positive(mock_user, mock_quiz, mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.write.return_value = True
        QuizHandler(mock_user, mock_quiz).remove_quiz()
