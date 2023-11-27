import sqlite3
from unittest.mock import MagicMock, patch

import pytest

from data_containers.last_transaction import LastTransaction
from data_containers.user import User, UserRole
from database import DBContext
from src.handler.auth import AuthHandler
from utils.crypt import hash_password


@pytest.fixture()
def mock_db_context():
    mock_db_ctx = MagicMock(spec=DBContext)
    mock_db_ctx.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_ctx.return_value = mock_db_ctx
    mock_db_ctx.__enter__.return_value = mock_db_ctx
    return mock_db_ctx


def get_mock_db_context_positive(
    mock_db_context, username="batman", password="Batman@123"
):
    mock_db_context_positive = mock_db_context
    mock_db_context_positive.read.return_value = (
        0,
        username,
        hash_password(password),
        UserRole.PLAYER,
    )
    mock_last_transaction = MagicMock(spec=LastTransaction)
    mock_last_transaction.rows_changed = 1
    mock_db_context_positive.write.return_value = mock_last_transaction
    return mock_db_context_positive


@pytest.fixture()
def mock_db_context_negative(mock_db_context):
    mock_db_context_negative = mock_db_context
    mock_db_context_negative.read.return_value = ()
    mock_last_transaction = MagicMock(spec=LastTransaction)
    mock_last_transaction.rows_changed = 0
    mock_db_context_negative.write.return_value = mock_last_transaction
    return mock_db_context_negative


@pytest.mark.parametrize(
    "username, password", [("batman", "Batman@123"), ("riddler", "Riddler@123")]
)
def test_sign_up_positive(username, password, mock_db_context):
    with patch(
        "src.handler.auth.DBContext",
        get_mock_db_context_positive(mock_db_context, username, password),
    ):
        auth_handler = AuthHandler(username, password)
        assert auth_handler.sign_up()


@pytest.mark.parametrize(
    "username, password", [("batman", "1234"), ("batman", "Batman@123")]
)
def test_sign_up_negative(username, password, mock_db_context_negative):
    with patch("src.handler.auth.DBContext", mock_db_context_negative):
        auth_handler = AuthHandler(username, password)
        assert not auth_handler.sign_up()


@pytest.mark.parametrize(
    "username, password", [("batman", "Batman@123"), ("riddler", "Riddler@123")]
)
def test_sign_in_positive(username, password, mock_db_context):
    with patch(
        "src.handler.auth.DBContext",
        get_mock_db_context_positive(mock_db_context, username, password),
    ):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert isinstance(user, User)


@pytest.mark.parametrize(
    "username, password",
    [
        ("", "Batman@123"),
        ("batman", ""),
        ("batman1", "batman@123"),
        ("batman", "batman@123"),
    ],
)
def test_sign_in_negative(username, password, mock_db_context_negative):
    with patch("src.handler.auth.DBContext", mock_db_context_negative):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)
