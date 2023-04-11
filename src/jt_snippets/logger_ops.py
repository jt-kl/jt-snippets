from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler, SysLogHandler
from pathlib import Path
from sys import stdout
from typing import Any, Optional, TextIO


def add_rotating_file_handler(
    logger,
    directory: Path,
    file: str = "application.log",
    level: int = DEBUG,
):
    """
    Add a RotatingFileHandler handler to logger

    Args:
        logger: Instance of logger
        directory: Directory path to store log file
        file: Name of log file
        level: Logging level
    """
    log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

    rotating_file_handler = RotatingFileHandler(
        directory.joinpath(file),
        maxBytes=10485760,
        backupCount=10,
    )
    rotating_file_handler.setLevel(level)
    rotating_file_handler.setFormatter(log_format)

    logger.addHandler(rotating_file_handler)


def create_console_stream_handler(
    stream: TextIO = stdout,
) -> StreamHandler:  # type: ignore
    """
    Creates a console stream handler

    Args:
        stream: Logging output stream
    """
    console_stream_handler = StreamHandler(stream)

    return console_stream_handler


def create_syslog_handler(
    address: tuple[str, int] = ("localhost", 514),
    **kwargs,
) -> SysLogHandler:
    """
    Creates a SysLog handler

    Args:
        address: Hostname and port number of SysLog host
    """
    syslog_handler = SysLogHandler(
        address,
        **kwargs,
    )

    return syslog_handler


def create_rotating_file_handler(
    directory: Path,
    filename: str = "application.log",
    maximum_file_size: int = 10485760,
    maximum_file_count: int = 10,
    **kwargs,
) -> RotatingFileHandler:
    """
    Creates a rotating file handler

    Args:
        directory: Directory path to store log file
        filename: Desired log file name
        maximum_file_size: Maximum file size before rolling over
        maximum_file_count: Maximum file count before rolling over
    """
    rotating_file_handler = RotatingFileHandler(
        directory.joinpath(filename),
        maxBytes=maximum_file_size,
        backupCount=maximum_file_count,
        **kwargs,
    )

    return rotating_file_handler


def create_logger(
    name: Optional[str] = None,
    level: int = DEBUG,
    handlers: list[Any] = [],
) -> Logger:
    """
    Create custom application logger

    Args:
        name: Name of logger
        level: Logging level
        handlers: Collection of handlers to add to logger
    """
    log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

    logger = getLogger(name)
    logger.setLevel(level)

    # Prevent logging from propagating to the root logger
    logger.propagate = False

    if not logger.hasHandlers():
        # Console stream handler
        console_stream_handler = StreamHandler(stdout)
        console_stream_handler.setLevel(level)
        console_stream_handler.setFormatter(log_format)

        logger.addHandler(console_stream_handler)

    for handler in handlers:
        handler.setLevel(level)
        handler.setFormatter(log_format)
        logger.addHandler(handler)

    # TODO: Add syslog handler

    return logger
