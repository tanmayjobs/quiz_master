from unittest.mock import patch
from src.utils.validators import Validators
import pytest


@pytest.mark.parametrize("username", ["", "1", "111", "??121", "batman?123"])
def test_get_username(username, monkeypatch):
    correct_username = "batman"
    with patch("builtins.input", side_effect=[username, correct_username]):
        assert correct_username == Validators.get_username()


@pytest.mark.parametrize("password", ["", "?????"])
def test_get_password(password, monkeypatch):
    correct_password = "Batman@123"
    with patch("pwinput.pwinput", side_effect=[password, correct_password]):
        assert correct_password == Validators.get_password()


@pytest.mark.parametrize("string", ["", "??", "!!!@!"])
def test_get_valid_string(string, monkeypatch):
    correct_string = "'What made you become a code developer?'."
    with patch("builtins.input", side_effect=[string, correct_string]):
        assert correct_string == Validators.get_valid_strings("")
