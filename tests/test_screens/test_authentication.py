from unittest.mock import patch

import pytest
from pytest import raises

from screens.authentication import AuthenticationScreen


@pytest.mark.parametrize("user_choice, func", [("1", "_sign_in"), ("2", "_sign_up")])
def test_authentication_home_screen_positive(user_choice, func):
    with raises(SystemExit):
        with patch.object(AuthenticationScreen, func) as mocked_func:
            with patch("builtins.input") as mock:
                mock.side_effect = [user_choice, "3"]
                AuthenticationScreen.menu_screen()
                mocked_func.assert_called_once()


@pytest.mark.parametrize("user_choice", ["10", "100", "asdas", "@123"])
def test_authentication_home_screen_negative(user_choice):
    with raises(SystemExit):
        with patch("builtins.input") as mock:
            mock.side_effect = [user_choice, "3"]
            AuthenticationScreen.menu_screen()
