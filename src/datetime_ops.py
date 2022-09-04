import datetime


def export_datetime(
    _datetime: datetime.datetime,
    _format: str,
):
    """
    Exports a datetime.datetime object to an ISO8601 or RFC3339 formatted string

    Args:
        _datetime: Object to be formatted
        format: Output format
    """
    assert _format.lower() in [
        "iso8601",
        "rfc3339",
    ], f"Invalid date/time format specified"

    if _format.lower() == "iso8601":
        return _datetime.isoformat("T")

    if _format.lower() == "rfc3339":
        return _datetime.isoformat(" ")
