from dataclasses import dataclass
from data_containers.types import QuizType


@dataclass
class Quiz:
    quiz_id: int | None
    quiz_name: str

    creator_id: int
    creator_name: str

    types: [QuizType]
