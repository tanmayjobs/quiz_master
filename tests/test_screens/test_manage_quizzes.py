import pytest
from unittest.mock import Mock, patch

from data_containers.user import User
from helpers.enums import UserRole
from screens.manage_quizzes import ManageQuizScreen


@pytest.mark.parametrize("user_choice, func", [("1", "_add_quiz_screen"), ("2", "_remove_quiz_screen"), ("3", "_modify_quiz_screen")])
def test_manage_quiz_screen(user_choice, func):
    mock_user = Mock(spec=User)
    mock_user.role = UserRole.CREATOR
    with patch.object(ManageQuizScreen, func) as mocked_screen:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = [user_choice, "4"]
            ManageQuizScreen(mock_user).manage_quizzes_screen()
            mocked_screen.assert_called_once()
