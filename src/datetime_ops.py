import datetime
import enum
import typing


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
