import sqlite3

import pytest
from unittest.mock import MagicMock, patch
from data_containers.user import User
from database import DBContext
from helpers.enums import UserRole
from src.controller.auth import AuthHandler


@pytest.fixture
def mock_db_context_positive():
    mock_db_context = MagicMock(spec=DBContext)
    mock_db_context.get.return_value = (
        0, "batman",
        b"$2b$12$PzZeVB9WVJnMqFexMAc1F.LJokCF.lJU5pPFpT9oOsKzD5nPIigEK",
        UserRole.PLAYER)
    mock_db_context.add.return_value = True
    mock_db_context.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_context.return_value = mock_db_context
    mock_db_context.__enter__.return_value = mock_db_context
    return mock_db_context


@pytest.fixture
def mock_db_context_negative():
    mock_db_context = MagicMock(spec=DBContext)
    mock_db_context.get.return_value = ()
    mock_db_context.add.return_value = False
    mock_db_context.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_context.return_value = mock_db_context
    mock_db_context.__enter__.return_value = mock_db_context
    return mock_db_context


def test_sign_up_positive(mock_db_context_positive):
    username = "batman"
    password = "Batman@123"
    with patch('src.controller.auth.DBContext', mock_db_context_positive):
        auth_handler = AuthHandler(username, password)
        assert auth_handler.sign_up()


def test_sign_up_negative_weak_password():
    username = "batman"
    password = "1234"
    auth_handler = AuthHandler(username, password)
    assert not auth_handler.sign_up()


def test_sign_up_negative_duplicate_username(mock_db_context_negative):
    username = "batman"
    password = "batman@123"
    with patch('src.controller.auth.DBContext', mock_db_context_negative):
        auth_handler = AuthHandler(username, password)
        assert not auth_handler.sign_up()


def test_sign_in_positive(mock_db_context_positive):
    username = "batman"
    password = "Batman@123"
    with patch('src.controller.auth.DBContext', mock_db_context_positive):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert isinstance(user, User)


def test_sign_in_negative_empty_username():
    username = ""
    password = "Batman@123"
    auth_handler = AuthHandler(username, password)
    user = auth_handler.sign_in()
    assert not isinstance(user, User)


def test_sign_in_negative_empty_password():
    username = "batman"
    password = ""
    auth_handler = AuthHandler(username, password)
    user = auth_handler.sign_in()
    assert not isinstance(user, User)


def test_sign_in_negative_wrong_username(mock_db_context_negative):
    username = "batman1"
    password = "Batman@123"
    with patch('src.controller.auth.DBContext', mock_db_context_negative):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)


def test_sign_in_negative_wrong_password(mock_db_context_positive):
    username = "batman"
    password = "Batman@1234"
    with patch('src.controller.auth.DBContext', mock_db_context_positive):
        auth_handler = AuthHandler(username, password)
        user = auth_handler.sign_in()
        assert not isinstance(user, User)
