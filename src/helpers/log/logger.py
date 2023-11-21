import logging
from logging import INFO, DEBUG, WARN, CRITICAL, ERROR

logging.basicConfig(
    level=logging.DEBUG,
    filename="helpers/log/server.log",
    filemode="a+",
    format="%(asctime)s %(levelname)-10s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)


class Logger:

    @staticmethod
    def log(lvl: int, msg: str, specific_name="server"):
        spc_logger = logging.getLogger(specific_name)
        spc_logger.log(lvl, msg)
