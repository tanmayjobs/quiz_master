from unittest.mock import patch, Mock

import pytest

from screens.admin import AdminScreen


@pytest.mark.parametrize(
    "user_choice, func",
    [
        ("1", "_add_creator_screen"),
        ("2", "_remove_user_screen"),
        ("3", "_remove_quiz_screen"),
    ],
)
def test_admin_home_screen(user_choice, func):
    with patch.object(AdminScreen, func) as mocked_func:
        with patch("builtins.input") as mock:
            mock.side_effect = [user_choice, "4"]
            AdminScreen(Mock()).home_screen()
            mocked_func.assert_called_once()
