import sqlite3
import pytest

from unittest.mock import MagicMock
from database import DBContext


@pytest.fixture(scope="module", autouse=True)
def mock_db_context():
    mock_db_ctx = MagicMock(spec=DBContext)
    mock_db_ctx.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_ctx.return_value = mock_db_ctx
    mock_db_ctx.__enter__.return_value = mock_db_ctx
    return mock_db_ctx
