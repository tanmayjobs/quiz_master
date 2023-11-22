from data_containers.user import User
from src.controller.auth import AuthHandler


def test_sign_up_positive():
    username = "batman"
    password = "Batman@123"
    assert AuthHandler(username, password).sign_up()


def test_sign_up_negative_weak_password():
    username = "batman"
    password = "1234"
    assert not AuthHandler(username, password).sign_up()


def test_sign_up_negative_duplicate_username():
    username = "batman"
    password = "batman@123"
    assert not AuthHandler(username, password).sign_up()


def test_sign_in_positive():
    username = "batman"
    password = "Batman@123"

    user = AuthHandler(username, password).sign_in()
    assert isinstance(user, User)


def test_sign_in_negative_empty_username():
    username = ""
    password = "Batman@123"
    assert AuthHandler(username, password).sign_in() is None


def test_sign_in_negative_empty_password():
    username = "batman"
    password = ""
    assert AuthHandler(username, password).sign_in() is None


def test_sign_in_negative_wrong_username():
    username = "batman1"
    password = "Batman@123"
    assert AuthHandler(username, password).sign_in() is None


def test_sign_in_negative_wrong_password():
    username = "batman"
    password = "Batman@1234"
    assert AuthHandler(username, password).sign_in() is None
