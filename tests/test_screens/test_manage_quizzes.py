import pytest
from unittest.mock import Mock, patch, MagicMock

from data_containers.user import User, UserRole
from screens.manage_quizzes import ManageQuizScreen


class TestManageQuizScreen:
    @pytest.mark.parametrize(
        "user_choice, func",
        [
            ("1", "_add_quiz_screen"),
            ("2", "_remove_quiz_screen"),
            ("3", "_modify_quiz_screen"),
        ],
    )
    def test_manage_quiz_screen(self, user_choice, func):
        mock_user = Mock(spec=User)
        mock_user.role = UserRole.CREATOR
        with patch.object(ManageQuizScreen, func) as mocked_screen:
            with patch("builtins.input") as mocked_input:
                mocked_input.side_effect = [user_choice, "4"]
                ManageQuizScreen(mock_user).manage_quizzes_screen()
                mocked_screen.assert_called_once()

    def test_select_quiz_screen_positive(self):
        with patch(
            "screens.manage_quizzes.QuizHandler.get_user_quizzes", return_value=[1]
        ):
            with patch("screens.manage_quizzes.CommonScreens") as mocked_common_screen:
                mocked_common_screen.select_from_list.return_value = 1
                assert ManageQuizScreen(MagicMock())._select_quiz_screen()

    def test_select_quiz_screen_negative(self):
        with patch(
            "screens.manage_quizzes.QuizHandler.get_user_quizzes", return_value=[1]
        ):
            with patch("screens.manage_quizzes.CommonScreens") as mocked_common_screen:
                mocked_common_screen.select_from_list.return_value = None
                assert not ManageQuizScreen(MagicMock())._select_quiz_screen()

    def test_select_quiz_type_positive(self):
        with patch(
            "screens.manage_quizzes.QuizHandler.defined_quiz_types", return_value=[]
        ):
            with patch("screens.manage_quizzes.CommonScreens") as mocked_common_screen:
                mocked_common_screen.select_multiple_from_list.return_value = [1]
                assert ManageQuizScreen._select_quiz_type()

    def test_select_quiz_type_negative(self):
        with patch(
            "screens.manage_quizzes.QuizHandler.defined_quiz_types", return_value=[]
        ):
            with patch("screens.manage_quizzes.CommonScreens") as mocked_common_screen:
                mocked_common_screen.select_multiple_from_list.return_value = None
                assert not ManageQuizScreen._select_quiz_type()
