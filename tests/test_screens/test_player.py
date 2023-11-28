from unittest.mock import patch, Mock

import pytest

from screens.player import PlayerScreen


class TestPlayerScreen:
    @pytest.mark.parametrize(
        "user_choice, func",
        [
            ("1", "_play_random_quiz"),
            ("2", "_explore_quiz"),
            ("3", "_show_player_records_screen"),
        ],
    )
    def test_player_home_screen(self, user_choice, func):
        with patch.object(PlayerScreen, func) as mocked_func:
            with patch("builtins.input") as mock:
                mock.side_effect = [user_choice, "4"]
                PlayerScreen(Mock()).home_screen()
                mocked_func.assert_called_once()
