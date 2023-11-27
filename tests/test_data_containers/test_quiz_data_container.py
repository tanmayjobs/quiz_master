from data_containers.quiz import Quiz
from data_containers.types import QuizType


def test_quiz_parse():
    quiz_id = 1
    quiz_name = "gotham"
    creator_id = 1
    creator_name = "riddler"
    data = (
        quiz_id,
        quiz_name,
        creator_id,
        creator_name,
        '{"type_id":1,"type_name":"Movie"},{"type_id":3,"type_name":"Book"}',
    )
    result = Quiz.parse_json(data)

    assert isinstance(result, Quiz)
