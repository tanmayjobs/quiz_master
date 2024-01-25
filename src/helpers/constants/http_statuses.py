from dataclasses import dataclass


@dataclass
class HTTPStatus:
    code: int
    status: str


class HTTPStatuses:
    OK = HTTPStatus(200, 'OK')
    CREATED = HTTPStatus(201, 'Created')
    ACCEPTED = HTTPStatus(202, 'Accepted')
    NO_CONTENT = HTTPStatus(204, 'No Content')
    MOVED_PERMANENTLY = HTTPStatus(301, 'Moved Permanently')
    FOUND = HTTPStatus(302, 'Found')
    SEE_OTHER = HTTPStatus(303, 'See Other')
    NOT_MODIFIED = HTTPStatus(304, 'Not Modified')
    BAD_REQUEST = HTTPStatus(400, 'Bad Request')
    UNAUTHORIZED = HTTPStatus(401, 'Unauthorized')
    FORBIDDEN = HTTPStatus(403, 'Forbidden')
    NOT_FOUND = HTTPStatus(404, 'Not Found')
    METHOD_NOT_ALLOWED = HTTPStatus(405, 'Method Not Allowed')
    CONFLICT = HTTPStatus(409, 'Conflict')
    UNPROCCESSABLE_ENTITY = HTTPStatus(422, 'Unprocessable Entity')
    INTERNAL_SERVER_ERROR = HTTPStatus(500, 'Internal Server Error')
    NOT_IMPLEMENTED = HTTPStatus(501, 'Not Implemented')
    SERVICE_UNAVAILABLE = HTTPStatus(503, 'Service Unavailable')
