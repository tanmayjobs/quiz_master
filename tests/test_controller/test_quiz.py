import sqlite3
from unittest.mock import Mock, MagicMock, patch

import pytest
from _pytest.python_api import raises

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


def mock_user(user_role=UserRole.PLAYER):
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


@pytest.mark.parametrize("user, quiz",
                         [(mock_user(UserRole.PLAYER), mock_quiz()), (mock_user(UserRole.ADMIN), mock_quiz())])
def test_add_quiz_negative(user, quiz):
    with raises(PermissionError):
        QuizHandler(user, quiz).add_quiz()


@pytest.mark.parametrize("user, quiz", [(mock_user(UserRole.CREATOR), mock_quiz())])
def test_add_quiz_positive(user, quiz, mock_db_context):
    with patch("src.handler.quiz.DBContext", mock_db_context):
        QuizHandler(user, quiz).add_quiz()


@pytest.mark.skip
def test_get_random_quiz_negative():
    with patch("src.handler.quiz.DBContext", mock_db_context):
        QuizHandler.get_random_quiz()
