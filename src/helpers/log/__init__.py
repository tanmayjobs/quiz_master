import logging
import os


logging.basicConfig(
    level=logging.NOTSET,
    filename=os.path.dirname(os.path.abspath(__file__)) + os.getenv("LOG_FILEPATH"),
    filemode=os.getenv("LOG_FILEMODE"),
    format=os.getenv("LOG_FORMAT"),
    datefmt=os.getenv("LOG_DATEFMT"),
)

logger = logging.getLogger()
