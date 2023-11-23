import pytest
from unittest.mock import patch
from screens.authentication import AuthenticationScreen


@pytest.mark.skip
def test_authentication_home_screen_1(monkeypatch):
    with patch('src.screens.authentication.AuthenticationScreen.sign_in') as sign_in_mock:
        monkeypatch.setattr('builtins.input', lambda _: '1')
        AuthenticationScreen.menu_screen()
        sign_in_mock.assert_called_once()
