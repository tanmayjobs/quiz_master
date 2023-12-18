from unittest.mock import patch

import pytest

from screens.common import CommonScreens


items = ["0", "1", "2", "3", "4", "5"]


def test_select_multiple_from_list():
    with patch("builtins.input", return_value="1,2,3,4"):
        assert CommonScreens.select_multiple_from_list(items) == items[:4]


@pytest.mark.parametrize("user_input", ["10", "@", "a", ".", "0.0", "0"])
def test_select_from_list_negative(user_input):
    with patch("builtins.input") as mock_input:
        mock_input.return_value = user_input
        assert not CommonScreens.select_from_list(items, "")


@pytest.mark.parametrize("user_input", ["1", "2", "5"])
def test_select_from_list_positive(user_input):
    with patch("builtins.input") as mock_input:
        mock_input.return_value = user_input
        assert items[int(user_input) - 1] == CommonScreens.select_from_list(items, "")
