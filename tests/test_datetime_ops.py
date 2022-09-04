import datetime
import unittest.mock

import pytest
from src.datetime_ops import export_datetime

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
export_datetime_happy = [
    (
        dict(
            _datetime=datetime.datetime(2022, 9, 1, 15, 30, 10),
            _format="iso8601",
        ),
        dict(
            result="2022-09-01T15:30:10",
        ),
    ),
    (
        dict(
            _datetime=datetime.datetime(2022, 8, 31, 9, 45, 25),
            _format="rfc3339",
        ),
        dict(
            result="2022-08-31 09:45:25",
        ),
    ),
]
export_datetime_sad = [
    (
        dict(
            _datetime=datetime.datetime(2022, 7, 15, 13, 10, 00),
            _format="rfc",
        ),
        dict(
            result=None,
            exception_type=AssertionError,
            exception_message=f"Invalid date/time format specified",
        ),
    ),
]

# endregion: PyTest parametrized variables


class TestDateTimeOps:
    @pytest.mark.parametrize("payload, expect", export_datetime_happy)
    def test_happy_export_datetime(self, payload, expect):
        result = export_datetime(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", export_datetime_sad)
    def test_sad_export_datetime(self, payload, expect):
        with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
            result = export_datetime(**payload)
