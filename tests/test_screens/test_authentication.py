from unittest.mock import patch

import pytest
from pytest import raises
from screens.authentication import AuthenticationScreen


@pytest.mark.parametrize("user_choice, func", [('1', 'sign_in'), ('2','sign_up')])
def test_authentication_home_screen_positive(user_choice, func):
    with raises(SystemExit):
        with patch.object(AuthenticationScreen, func) as mocked_sign_in:
            with patch('builtins.input') as mock:
                mock.return_value = user_choice
                mock.side_effect = '3'
                AuthenticationScreen.menu_screen()
                mocked_sign_in.assert_called_once()
