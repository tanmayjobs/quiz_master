import sqlite3
from unittest.mock import MagicMock, Mock

import pytest

from data_containers.user import User
from database import DBContext
from helpers.enums import UserRole


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
    mocked_user.username = "alfred"
    mocked_user.role = UserRole.ADMIN
    return mocked_user


def test_add_user_negative(mock_user):
    ...
