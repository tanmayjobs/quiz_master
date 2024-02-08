import logging
import os

from flask import request


class RequestLogHandler(logging.FileHandler):
    default_filename = os.path.dirname(os.path.abspath(__file__)) + os.getenv("REQUEST_LOG_FILEPATH")

    def __init__(self, filename=None, mode='a', encoding=None, delay=False, errors=None):
        super().__init__(filename or self.default_filename, mode, encoding, delay, errors)

    def format(self, record):
        record.request_id = (request and request.request_id) or None
        record.url = (request and request.url) or None
        record.remote_addr = (request and request.remote_addr) or None

        return super().format(record)
