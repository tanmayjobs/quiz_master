import json
from dataclasses import dataclass

from helpers.constants import Strings
from data_containers.types import QuizType


@dataclass
class Quiz:
    quiz_id: int | None
    quiz_name: str

    creator_id: int
    creator_name: str

    types: [QuizType]

    @staticmethod
    def parse_json(json_data):
        quiz_id, quiz_name, creator_id, creator_name, types = json_data
        types = Strings.ARRAY.format(types)
        types_json = json.loads(types)

        types = [
            QuizType.parse_json(
                each_type_json
            )
            for each_type_json in types_json
        ]

        quiz = Quiz(quiz_id, quiz_name, creator_id, creator_name, types)
        return quiz
