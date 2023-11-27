import sqlite3
from unittest.mock import MagicMock, patch

import pytest

from data_containers.quiz_record import QuizRecord
from handler.quiz_record import QuizRecordHandler
from src.database import DBContext


@pytest.fixture()
def mock_db_context():
    mock_db_ctx = MagicMock(spec=DBContext)
    mock_db_ctx.connection = MagicMock(spec=sqlite3.Connection)
    mock_db_ctx.return_value = mock_db_ctx
    mock_db_ctx.__enter__.return_value = mock_db_ctx
    return mock_db_ctx


@pytest.mark.parametrize("quiz_records", [tuple(), ((8, 'pain', 10, 'python', 0, 2, '2023-11-27 04:24:04'),
                                                    (8, 'pain', 6, 'cyber security', 3, 3, '2023-11-22 09:44:13'),)])
def test_get_user_records(quiz_records, mock_db_context):
    with patch("src.handler.quiz_record.DBContext", mock_db_context):
        mock_user = MagicMock()
        mock_user.user_id = 1
        mock_db_context.read.return_value = quiz_records
        for each_record in QuizRecordHandler.get_user_records(mock_user):
            assert isinstance(each_record, QuizRecord)


@pytest.mark.parametrize("quiz_records", [tuple(), ((4, 'riddler', 6, 'cyber security', 3, 3, '2023-11-23 07:52:13'),
                                                    (8, 'pain', 6, 'cyber security', 3, 3, '2023-11-22 09:44:13'),
                                                    (2, 'batman', 6, 'cyber security', 2, 3, '2023-11-20 06:47:40'),
                                                    (11, 'bad_guy', 6, 'cyber security', 1, 3, '2023-11-20 06:43:15'))])
def test_quiz_top_records(quiz_records, mock_db_context):
    with patch("src.handler.quiz_record.DBContext", mock_db_context):
        mock_db_context.read.return_value = quiz_records
        for each_record in QuizRecordHandler.quiz_top_records(3):
            assert isinstance(each_record, QuizRecord)
