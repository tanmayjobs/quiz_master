from unittest.mock import patch, Mock

import pytest

from screens.creator import CreatorScreen


@pytest.mark.parametrize(
    "user_choice, func",
    [
        ("1", "_play_random_quiz"),
        ("2", "_explore_quiz"),
        ("3", "_show_player_records_screen"),
        ("4", "_manage_quiz_screen"),
    ],
)
def test_creator_home_screen(user_choice, func):
    with patch.object(CreatorScreen, func) as mocked_func:
        with patch("builtins.input") as mock:
            mock.side_effect = [user_choice, "5"]
            CreatorScreen(Mock()).home_screen()
            mocked_func.assert_called_once()
