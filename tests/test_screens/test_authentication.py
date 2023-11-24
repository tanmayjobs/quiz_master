import pytest
from unittest.mock import patch, Mock
from screens.authentication import AuthenticationScreen


@pytest.mark.skip
def test_authentication_home_screen_1(monkeypatch):
    monkeypatch.setattr('src.screens.authentication.AuthenticationScreen.sign_in', lambda _: True)
    monkeypatch.setattr('builtins.input', lambda _: '1')
    AuthenticationScreen.menu_screen()