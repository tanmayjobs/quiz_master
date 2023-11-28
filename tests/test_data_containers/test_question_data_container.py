from data_containers.question import Question


class TestQuestionParse:
    def test_question_parse(self):
        data = (
            24,
            "Is polymorphism possible in python?",
            '{"option":"Yes","is_correct":0},{"option":"No","is_correct":0},{"option":"Yes and No, it\'s complicated","is_correct":1},{"option":"Polymorphism in python is called duck typing","is_correct":0}',
        )
        result = Question.parse_json(data)
        assert isinstance(result, Question)
