from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import stdout
from typing import Optional


def create_logger(
    name: Optional[str] = __name__,
    directory: Optional[Path] = None,
    level: int = DEBUG,
) -> Logger:
    """
    Create custom application logger

    Args:
        directory: Storage path for log file
    """
    logger = getLogger(name)
    logger.setLevel(level)

    log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

    if directory:
        directory.mkdir(exist_ok=True, parents=True)

        # Log file handler
        log_file = directory.joinpath("application.log")

        file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=10)

        file_handler.setLevel(level)
        file_handler.setFormatter(log_format)

        logger.addHandler(file_handler)

    # Stream handler
    # stream_handler = StreamHandler(stdout)

    # stream_handler.setLevel(level)
    # stream_handler.setFormatter(log_format)

    # logger.addHandler(stream_handler)

    # TODO: Add syslog handler

    return logger
