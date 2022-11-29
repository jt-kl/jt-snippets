from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import stdout
from typing import Optional


def create_logger(
    name: Optional[str] = __name__,
    directory: Optional[Path] = None,
    file: str = "application.log",
    level: int = DEBUG,
) -> Logger:
    """
    Create custom application logger

    Args:
        path: Directory path to store log file
        file: Name of log file
    """
    logger = getLogger(name)
    logger.setLevel(level)

    log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

    if not logger.hasHandlers():
        # Prevent logging from propagating to the root logger
        logger.propagate = False

        # Stream handler
        stream_handler = StreamHandler(stdout)

        stream_handler.setLevel(level)
        stream_handler.setFormatter(log_format)

        logger.addHandler(stream_handler)

        if directory:
            directory.mkdir(exist_ok=True, parents=True)

            # Log file handler
            log_file = directory.joinpath(file)

            file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=10)

            file_handler.setLevel(level)
            file_handler.setFormatter(log_format)

            logger.addHandler(file_handler)

    # TODO: Add syslog handler

    return logger
