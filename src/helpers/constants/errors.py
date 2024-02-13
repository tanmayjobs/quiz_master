from helpers.constants import Strings


class Errors:
    INVALID_CREDENTIALS = "username and password did not match!"
    USERNAME_ALREADY_EXISTS = "user with name {} already exists!"
    QUIZ_ALREADY_EXISTS = "quiz with name {} already exists!"
    TAG_ALREADY_EXISTS = "tag with name {} already exists!"
    NOT_FOUND = "{res} with {res} id {id} not found!"
    USER_NOT_FOUND = NOT_FOUND.format_map({"res": Strings.USER, "id": "{id}"})
    QUIZ_NOT_FOUND = NOT_FOUND.format_map({"res": Strings.QUIZ, "id": "{id}"})
    TAG_NOT_FOUND = NOT_FOUND.format_map({"res": Strings.TAG, "id": "{id}"})
    QUESTION_NOT_FOUND = NOT_FOUND.format_map({"res": Strings.QUESTION, "id": "{id}"})
    INVALID_QUIZ_ANSWERS = "the quiz response is invalid!"
    OPTION_NOT_FOUND = NOT_FOUND.format_map({"res": Strings.OPTION, "id": "{id}"})
    NOT_CREATOR_OF_QUIZ = "you are not the creator of the quiz!"
    NOT_ENOUGH_PERMISSIONS = "you don't have enough permissions"
    TOKEN_NOT_FRESH = "you need to re-authenticate yourself!"
    BLOCKED_TOKEN = "provided token is blocked"
    TOKEN_NOT_PROVIDED = "token not provided!"
    EXPIRED_TOKEN = "provided token is expired!"
