from unittest.mock import Mock

import pytest

from data_containers.last_transaction import LastTransaction
from database import DBContext


@pytest.fixture()
def mock_cursor():
    mock_cursor = Mock()
    mock_cursor.execute.return_value.fetchone.return_value = True
    mock_cursor.execute.return_value.fetchall.return_value = True
    return mock_cursor


@pytest.fixture()
def mock_database(mock_cursor):
    mocked_database = Mock()
    mocked_database.connection.cursor.return_value = mock_cursor
    return mocked_database


class TestDBContext:
    def test_read(self, mock_database):
        with DBContext(mock_database) as database_access_object:
            assert database_access_object.read("")

    def test_write(self, mock_database):
        with DBContext(mock_database) as database_access_object:
            assert isinstance(database_access_object.write(""), LastTransaction)
