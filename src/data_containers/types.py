from dataclasses import dataclass

from helpers.constants import Strings


@dataclass
class QuizType:
    type_id: int
    type_name: str

    @staticmethod
    def parse_json(json_data):
        quiz_type = QuizType(json_data[Strings.TYPE_ID], json_data[Strings.TYPE_NAME])

        return quiz_type
