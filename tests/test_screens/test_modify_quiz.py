import pytest
from unittest.mock import Mock, patch

from screens.modify_quiz import ModifyQuizScreen


@pytest.mark.parametrize(
    "user_choice, func",
    [
        ("1", "_list_all_questions_screen"),
        ("2", "_add_question_screen"),
        ("3", "_remove_question_screen"),
    ],
)
def test_modify_quiz_screen(user_choice, func):
    with patch.object(ModifyQuizScreen, func) as mocked_screen:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = [user_choice, "4"]
            ModifyQuizScreen(Mock(), Mock()).modify_quiz_screen()
            mocked_screen.assert_called_once()
