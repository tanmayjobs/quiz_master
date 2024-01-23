from dataclasses import dataclass

from helpers.constants import Strings


@dataclass
class QuizTag:
    id: str
    tag_name: str | None

    @staticmethod
    def parse_json(json_data):
        quiz_type = QuizTag(json_data[Strings.TYPE_ID], json_data[Strings.TYPE_NAME])
        return quiz_type
