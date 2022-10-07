import datetime
import enum
import typing
import zoneinfo


class DateTimeFormat(enum.Enum):
    """
    Date Time Format
    """

    ISO8601 = "iso8601"
    RFC3339 = "rfc3339"


def export_datetime(
    _datetime: datetime.datetime,
    _format: typing.Union[DateTimeFormat, str],
):
    """
    Exports a datetime.datetime object to an ISO8601 or RFC3339 formatted string

    Args:
        _datetime: Object to be formatted
        format: Output format
    """
    if isinstance(_format, DateTimeFormat):
        if _format.value == "iso8601":
            return _datetime.isoformat("T")
        else:
            return _datetime.isoformat(" ")

    else:
        return _datetime.strftime(_format)


def to_datetime(
    timestamp: typing.Union[int, float],
) -> datetime.datetime:
    """
    Converts timestamp to datetime.datetime

    Args:
        timestamp: Timestamp value
    """
    _datetime = None

    try:
        _datetime = datetime.datetime.fromtimestamp(timestamp)
    except ValueError:
        # Converts timestamp from milliseconds to seconds
        _datetime = datetime.datetime.fromtimestamp(timestamp / 1000)

    return _datetime


def is_weekday(
    day: typing.Union[datetime.datetime, datetime.date],
) -> bool:
    """
    Check if a given day is a weekday or otherwise

    Args:
        day: Date/DateTime to be inspected
    """
    if day.isoweekday() not in [1, 2, 3, 4, 5]:
        return False

    return True


def is_weekend(
    day: typing.Union[datetime.datetime, datetime.date],
) -> bool:
    """
    Check if a given day is a weekend or otherwise

    Args:
        day: Date/DateTime to be inspected
    """
    if day.isoweekday() not in [6, 7]:
        return False

    return True
