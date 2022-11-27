from datetime import date, datetime, timedelta
from enum import Enum
from typing import Optional, Union


class DateTimeFormat(Enum):
    """
    Date Time Format
    """

    ISO8601 = "iso8601"
    RFC3339 = "rfc3339"


def export_datetime(
    _datetime: datetime,
    _format: Union[DateTimeFormat, str],
):
    """
    Exports a datetime object to an ISO8601 or RFC3339 formatted string

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
    timestamp: Union[int, float],
) -> datetime:
    """
    Converts timestamp to datetime

    Args:
        timestamp: Timestamp value
    """
    _datetime = None

    try:
        _datetime = datetime.utcfromtimestamp(timestamp)
    except ValueError:
        # Converts timestamp from milliseconds to seconds
        _datetime = datetime.utcfromtimestamp(timestamp / 1000)

    return _datetime


def is_weekday(
    day: Union[datetime, date],
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
    day: Union[datetime, date],
) -> bool:
    """
    Check if a given day is a weekend or otherwise

    Args:
        day: Date/DateTime to be inspected
    """
    if day.isoweekday() not in [6, 7]:
        return False

    return True


def get_weekdays(
    ranges: Optional[tuple[date, date]] = None,
):
    """
    Get weekdays of given/current month

    Args:
        ranges: Start and end date ranges
    """
    weekdays = []

    if not ranges:
        day = date(
            year=date.today().year,
            month=date.today().month,
            day=1,
        )

        month = day.month

        while day.month == month:
            if day.isoweekday() in [1, 2, 3, 4, 5]:
                weekdays.append(day)

            day += timedelta(days=1)
    else:
        range_start, range_end = ranges

        while range_end > range_start:
            if range_start.isoweekday() in [1, 2, 3, 4, 5]:
                weekdays.append(range_start)

            range_start += timedelta(days=1)

    return weekdays


def get_weekends(
    ranges: Optional[tuple[date, date]] = None,
):
    """
    Get weekends of given/current month

    Args:
        ranges: Start and end date ranges
    """
    weekends = []

    if not ranges:
        day = date(
            year=date.today().year,
            month=date.today().month,
            day=1,
        )

        month = day.month

        while day.month == month:
            if day.isoweekday() in [6, 7]:
                weekends.append(day)

            day += timedelta(days=1)
    else:
        range_start, range_end = ranges

        while range_end > range_start:
            if range_start.isoweekday() in [6, 7]:
                weekends.append(range_start)

            range_start += timedelta(days=1)

    return weekends
