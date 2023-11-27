from unittest.mock import patch, Mock

import pytest

from data_containers.quiz import Quiz
from screens.quiz_screen import QuizScreen, QuizRecordHandler


@pytest.fixture()
def mock_quiz():
    mocked_quiz = Mock(spec=Quiz)
    mocked_quiz.quiz_id = ""
    mocked_quiz.quiz_name = ""
    mocked_quiz.creator_name = ""
    return mocked_quiz


def test_play_screen_negative(mock_quiz):
    with patch("src.handler.questions.QuestionHandler.get_quiz_questions") as mocked_questions:
        with patch("src.screens.quiz_screen.QuizScreen.play_quiz") as mocked_screen:
            mocked_questions.return_value = []
            QuizScreen.play_screen(Mock(), mock_quiz)
            mocked_screen.assert_not_called()


def test_play_screen_positive(mock_quiz, monkeypatch):
    with patch.object(QuizScreen, "play_quiz") as mocked_screen:
        monkeypatch.setattr(QuizScreen, "show_quiz_result", lambda _: True)
        monkeypatch.setattr(QuizRecordHandler, "add_quiz_record", lambda _: True)
        with patch("src.screens.quiz_screen.QuestionHandler.get_quiz_questions") as mocked_questions:
            mocked_questions.return_value = [1, 2, 3]
            QuizScreen.play_screen(Mock(), mock_quiz)
            mocked_screen.assert_called_once()
