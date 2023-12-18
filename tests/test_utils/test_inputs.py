import pytest

from unittest.mock import patch
from utils.inputs import get_username, get_password, get_string


@pytest.mark.parametrize("username", ["121", "1112?", "batmann!#?"])
def test_get_username(username):
    with patch("src.utils.inputs.Validators.get_username") as mocked_validator:
        with patch("builtins.input") as mocked_input:
            correct_username = "batman"
            mocked_input.side_effect = [username, correct_username]
            mocked_validator.side_effect = [None, correct_username]
            assert correct_username == get_username()


@pytest.mark.parametrize("password", ["121", "1112", "bat123", "password"])
def test_get_password(password):
    with patch("src.utils.inputs.Validators.get_password") as mocked_validator:
        with patch("pwinput.pwinput") as mocked_input:
            correct_password = "Batman@123"
            mocked_input.side_effect = [password, correct_password]
            mocked_validator.side_effect = [None, correct_password]
            assert correct_password == get_password()


@pytest.mark.parametrize("string", ["121", "1112", "123", ""])
def test_get_string(string):
    with patch("src.utils.inputs.Validators.get_valid_string") as mocked_validator:
        with patch("builtins.input") as mocked_input:
            correct_string = "Don't think this is the end?"
            mocked_input.side_effect = [string, correct_string]
            mocked_validator.side_effect = [None, correct_string]
            assert correct_string == get_string("")
