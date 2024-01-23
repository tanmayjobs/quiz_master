import json
from dataclasses import dataclass

from data_containers.types import QuizTag
from helpers.constants import Strings


@dataclass
class Quiz:
    quiz_id: str | None
    quiz_name: str

    creator_id: int
    creator_name: str | None

    tags: [QuizTag]

    @staticmethod
    def parse_json(json_data):
        quiz_id, quiz_name, creator_id, creator_name, tags = json_data
        tags = Strings.ARRAY.format(tags)
        tags_json = json.loads(tags)

        tags = [QuizTag.parse_json(each_tag_json) for each_tag_json in tags_json]

        quiz = Quiz(quiz_id, quiz_name, creator_id, creator_name, tags)
        return quiz
