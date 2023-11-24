import sqlite3
from unittest.mock import Mock, MagicMock, patch

import pytest
from pytest import raises

from data_containers.quiz import Quiz
from data_containers.user import User
from database import DBContext
from helpers.enums import UserRole
from src.handler.quiz import QuizHandler


@pytest.fixture()
def mock_db_context():
    mock_db_ctx = MagicMock(spec=DBContext)
    mock_db_ctx.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_ctx.return_value = mock_db_ctx
    mock_db_ctx.__enter__.return_value = mock_db_ctx
    return mock_db_ctx


def mock_user(user_role=UserRole.CREATOR):
    mocked_user = Mock(spec=User)
    mocked_user.username = "batman"
    mocked_user.role = user_role
    return mocked_user


def mock_quiz():
    mocked_quiz = Mock(spec=Quiz)
    mocked_quiz.quiz_name = ""
    mocked_quiz.creator_id = ""
    mocked_quiz.types = ""
    return mocked_quiz


def test_add_quiz_negative():
    user = mock_user()
    with raises(ValueError):
        QuizHandler(user).add_quiz()


@pytest.mark.parametrize("user, quiz", [(mock_user(UserRole.CREATOR), mock_quiz())])
def test_add_quiz_positive(user, quiz, mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        QuizHandler(user, quiz).add_quiz()


def test_get_random_quiz_negative(mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        mock_db_context.read.return_value = None
        expected_value = None
        assert expected_value == QuizHandler.get_random_quiz()


def test_get_random_quiz_positive(mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        quiz_data = (1, "Quiz Name", 1, "Creator Name", '{"type_id":1,"type_name":"Movie"}')
        mock_db_context.read.return_value = quiz_data
        expected_value = Quiz.parse_json(quiz_data)
        assert expected_value == QuizHandler.get_random_quiz()


def test_get_user_quizzes_negative():
    ...
