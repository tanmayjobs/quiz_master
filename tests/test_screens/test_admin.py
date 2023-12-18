from unittest.mock import patch, Mock, MagicMock

import pytest

from data_containers.user import User, UserRole
from screens.admin import AdminScreen


@pytest.fixture()
def mock_user():
    mocked_user = Mock(spec=User)
    mocked_user.username = "alfred"
    mocked_user.role = UserRole.ADMIN
    return mocked_user


class TestAdminScreen:
    @pytest.mark.parametrize(
        "user_choice, func",
        [
            ("1", "_add_creator_screen"),
            ("2", "_remove_user_screen"),
            ("3", "_remove_quiz_screen"),
        ],
    )
    def test_admin_home_screen(self, user_choice, func):
        with patch.object(AdminScreen, func) as mocked_func:
            with patch("builtins.input") as mock:
                mock.side_effect = [user_choice, "4"]
                AdminScreen(Mock()).home_screen()
                mocked_func.assert_called_once()

    def test_remove_quiz_screen_negative(self):
        with patch("screens.admin.QuizHandler") as mocked_quiz_handler:
            with patch("screens.admin.CommonScreens") as mocked_common_screen:
                mocked_common_screen.select_from_list.return_value = None
                mocked_quiz_handler.get_all_quizzes = []
                assert not AdminScreen(MagicMock())._remove_quiz_screen()
