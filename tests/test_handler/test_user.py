import sqlite3
from unittest.mock import MagicMock, Mock, patch

import pytest

from data_containers.last_transaction import LastTransaction
from data_containers.user import User, UserRole
from database import DBContext
from src.handler.user import UserHandler


@pytest.fixture()
def mock_user():
    mocked_user = Mock(spec=User)
    mocked_user.username = "alfred"
    mocked_user.role = UserRole.ADMIN
    return mocked_user


class TestUserHandler:
    def test_add_user_negative(self, mock_user, mock_db_context):
        with patch("src.handler.user.DBContext", mock_db_context):
            mock_last_transaction = MagicMock(spec=LastTransaction)
            mock_last_transaction.rows_changed = 0
            mock_db_context.write.return_value = mock_last_transaction
            assert not UserHandler(mock_user).add_user("", "")

    def test_add_user_positive(self, mock_user, mock_db_context):
        with patch("src.handler.user.DBContext", mock_db_context):
            mock_last_transaction = MagicMock(spec=LastTransaction)
            mock_last_transaction.rows_changed = 1
            mock_db_context.write.return_value = mock_last_transaction
            assert UserHandler(mock_user).add_user("", "")

    @pytest.mark.parametrize(
        "all_users", [[], [(1, "username", "hashed_password", UserRole.PLAYER)]]
    )
    def test_get_all_users(self, all_users, mock_user, mock_db_context):
        with patch("src.handler.user.DBContext", mock_db_context):
            mock_db_context.read.return_value = all_users
            assert len(all_users) == len(UserHandler(mock_user).get_all_users())

    def test_remove_user_negative(self, mock_user, mock_db_context):
        with patch("src.handler.user.DBContext", mock_db_context):
            mock_last_transaction = MagicMock(spec=LastTransaction)
            mock_last_transaction.rows_changed = 0
            mock_db_context.write.return_value = mock_last_transaction
            assert not UserHandler(mock_user).remove_user(mock_user())

    def test_remove_user_positive(self, mock_user, mock_db_context):
        with patch("src.handler.user.DBContext", mock_db_context):
            mock_last_transaction = MagicMock(spec=LastTransaction)
            mock_last_transaction.rows_changed = 1
            mock_db_context.write.return_value = mock_last_transaction
            assert UserHandler(mock_user).remove_user(mock_user())
