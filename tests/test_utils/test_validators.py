import pytest

import src.utils.validators as Validators


class TestValidators:
    @pytest.mark.parametrize("username", ["", "1", "111", "??121", "batman?123", "2pac"])
    def test_get_username_negative(self, username):
        assert not Validators.get_username(username)

    @pytest.mark.parametrize("username", ["eminem", "tupac", "batman123", "gara"])
    def test_get_username_positive(self, username):
        assert Validators.get_username(username)

    @pytest.mark.parametrize("password", ["", "?????"])
    def test_get_password_negative(self, password, monkeypatch):
        assert not Validators.get_password(password)

    @pytest.mark.parametrize("password", ["Batman@123", "Als#123"])
    def test_get_password_positive(self, password, monkeypatch):
        assert Validators.get_password(password)

    @pytest.mark.parametrize("string", ["", "??", "!!!@!"])
    def test_get_valid_string_negative(self, string, monkeypatch):
        assert not Validators.get_valid_strings(string)

    @pytest.mark.parametrize(
        "string",
        ["So, how was your day", "Don't think this is the end?", "All of the Above."],
    )
    def test_get_valid_string_positive(self, string, monkeypatch):
        assert Validators.get_valid_strings(string)
