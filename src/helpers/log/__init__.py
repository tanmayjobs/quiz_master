import logging
import os

from helpers.log.request_log_handler import RequestLogHandler

logging.basicConfig(
    level=logging.NOTSET,
    filename=os.path.dirname(os.path.abspath(__file__)) + os.getenv("LOG_FILEPATH"),
    filemode=os.getenv("LOG_FILEMODE"),
    format=os.getenv("SYSTEM_LOG_FORMAT"),
    datefmt=os.getenv("LOG_DATEFMT"),
)


def set_request_logger():
    request_logger = logging.Logger(__name__)

    _handler = RequestLogHandler()
    _handler.setFormatter(logging.Formatter(os.getenv("REQUEST_LOG_FORMAT")))
    request_logger.addHandler(_handler)

    return request_logger


request_logger = set_request_logger()
__all__ = ['request_logger']
