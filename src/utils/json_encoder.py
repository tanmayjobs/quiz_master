from enum import Enum
from flask.json.provider import DefaultJSONProvider

from helpers.exceptions import CustomException


class CustomJSONEncoder(DefaultJSONProvider):
    def default(self, obj):
        print("asdo")
        if isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, CustomException):
            print(obj)
            return obj.dump()
        return super().default(obj)
