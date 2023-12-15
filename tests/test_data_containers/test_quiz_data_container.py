from data_containers.quiz import Quiz


class TestQuizParse:
    def test_quiz_parse(self):
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
