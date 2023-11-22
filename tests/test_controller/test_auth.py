import pytest
from unittest.mock import Mock, patch

from data_containers.user import User
from database import Database
from helpers.enums import UserRole
from src.controller.auth import AuthHandler


@pytest.fixture
def mock_database_positive():
    mock_db = Mock(spec=Database)
    mock_db.get.return_value = (0, "batman", b"$2b$12$PzZeVB9WVJnMqFexMAc1F.LJokCF.lJU5pPFpT9oOsKzD5nPIigEK",  UserRole.PLAYER)
    mock_db.add.return_value = True
    return mock_db


@pytest.fixture
def mock_database_negative():
    mock_db = Mock(spec=Database)
    mock_db.get.return_value = ()
    mock_db.add.return_value = False
    return mock_db


def test_sign_up_positive(mock_database_positive):
    username = "batman"
    password = "Batman@123"

    with patch('src.controller.auth.database', mock_database_positive):
        auth_handler = AuthHandler(username, password)
        assert auth_handler.sign_up()


def test_sign_up_negative_weak_password(mock_database_negative):
    username = "batman"
    password = "1234"
    with patch('src.controller.auth.database', mock_database_negative):
        auth_handler = AuthHandler(username, password)
        assert not auth_handler.sign_up()


def test_sign_up_negative_duplicate_username(mock_database_negative):
    username = "batman"
    password = "batman@123"
    with patch('src.controller.auth.database', mock_database_negative):
        auth_handler = AuthHandler(username, password)
        assert not auth_handler.sign_up()


def test_sign_in_positive(mock_database_positive):
    username = "batman"
    password = "Batman@123"
    with patch('src.controller.auth.database', mock_database_positive):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert isinstance(user, User)


def test_sign_in_negative_empty_username(mock_database_negative):
    username = ""
    password = "Batman@123"
    with patch('src.controller.auth.database', mock_database_negative):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)


def test_sign_in_negative_empty_password(mock_database_negative):
    username = "batman"
    password = ""
    with patch('src.controller.auth.database', mock_database_negative):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)


def test_sign_in_negative_wrong_username(mock_database_negative):
    username = "batman1"
    password = "Batman@123"
    with patch('src.controller.auth.database', mock_database_negative):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)


def test_sign_in_negative_wrong_password(mock_database_positive):
    username = "batman"
    password = "Batman@1234"
    with patch('src.controller.auth.database', mock_database_positive):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)
