from datetime import time
from logging import DEBUG, Formatter, Handler, Logger, StreamHandler, getLogger
from logging.handlers import (
    RotatingFileHandler,
    SysLogHandler,
    TimedRotatingFileHandler,
)
from pathlib import Path
from typing import TextIO


def create_stream_handler(
    stream: TextIO | None = None,
    level: int = DEBUG,
    format: str | None = None,
) -> StreamHandler:
    """
    Creates a console stream handler

    Args:
        stream: Logging output stream
        level: Logging level
        format: Logging format
    """
    handler = StreamHandler(stream)
    handler.setLevel(level)

    if format:
        handler.setFormatter(Formatter(format))
    else:
        handler.setFormatter(
            Formatter(
                (
                    "%(asctime)s|"
                    "%(levelname)-8s|"
                    "%(module)s:"
                    "%(funcName)s:"
                    "%(lineno)d - %(message)s"
                )
            )
        )

    return handler


def create_rotating_file_handler(
    directory: Path,
    filename: str = "application.log",
    level: int = DEBUG,
    format: str | None = None,
    maximum_file_size: int = 10485760,
    maximum_file_count: int = 10,
    **kwargs,
) -> RotatingFileHandler:
    """
    Creates a rotating file handler

    Args:
        directory: Log directory
        filename: Log file name
        level: Logging level
        format: Logging format
        maximum_file_size: Maximum file size before rolling over
        maximum_file_count: Maximum file count before rolling over
    """
    handler = RotatingFileHandler(
        directory.joinpath(filename),
        maxBytes=maximum_file_size,
        backupCount=maximum_file_count,
        **kwargs,
    )
    handler.setLevel(level)

    if format:
        handler.setFormatter(Formatter(format))
    else:
        handler.setFormatter(
            Formatter(
                (
                    "%(asctime)s|"
                    "%(levelname)-8s|"
                    "%(module)s:"
                    "%(funcName)s:"
                    "%(lineno)d - %(message)s"
                )
            )
        )

    return handler


def create_timed_rotating_file_handler(
    directory: Path,
    filename: str = "application.log",
    level: int = DEBUG,
    format: str | None = None,
    interval: int = 24,
    rollover: time = time(0, 0, 0),
    maximum_file_count: int = 31,
) -> TimedRotatingFileHandler:
    """
    Creates a timed rotating file handler

    Args:
        directory: Log directory
        filename: Log file name
        level: Logging level
        interval: Log file rollover interval
        rollover: Log file rollover time
        format: Logging format
        maximum_file_count: Maximum file count before rolling over
    """
    handler = TimedRotatingFileHandler(
        directory.joinpath(filename),
        interval=interval,
        backupCount=maximum_file_count,
        atTime=rollover,
    )
    handler.setLevel(level)

    if format:
        handler.setFormatter(Formatter(format))
    else:
        handler.setFormatter(
            Formatter(
                (
                    "%(asctime)s|"
                    "%(levelname)-8s|"
                    "%(module)s:"
                    "%(funcName)s:"
                    "%(lineno)d - %(message)s"
                )
            )
        )

    return handler


def create_syslog_handler(
    address: tuple[str, int] = ("localhost", 514),
    level: int = DEBUG,
    format: str | None = None,
    **kwargs,
) -> SysLogHandler:
    """
    Creates a Syslog handler

    Args:
        address: Syslog hostname and port number
        level: Logging level
        format: Logging format
    """
    handler = SysLogHandler(address, **kwargs)
    handler.setLevel(level)

    if format:
        handler.setFormatter(Formatter(format))
    else:
        handler.setFormatter(
            Formatter(
                (
                    "%(asctime)s|"
                    "%(levelname)-8s|"
                    "%(module)s:"
                    "%(funcName)s:"
                    "%(lineno)d - %(message)s"
                )
            )
        )

    return handler


def create_logger(
    name: str | None = None,
    level: int = DEBUG,
    format: str | None = None,
    handlers: list[Handler] = list(),
) -> Logger:
    """
    Creates a logger

    Args:
        name: Logger name
        level: Logging level
        format: Logging format
        handlers: Collection of logging handlers
    """
    logger = getLogger(name)
    logger.setLevel(level)

    # Prevent logging from propagating to the root logger
    logger.propagate = False

    for handler in handlers:
        if format:
            handler.setFormatter(Formatter(format))

        logger.addHandler(handler)

    return logger
