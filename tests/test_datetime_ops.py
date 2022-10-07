import datetime
import unittest.mock

import pytest
from src.jt_snippets.datetime_ops import DateTimeFormat, export_datetime

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
export_datetime_happy = [
    (
        dict(
            _datetime=datetime.datetime(2022, 9, 1, 15, 30, 10),
            _format=DateTimeFormat.ISO8601,
        ),
        dict(
            result="2022-09-01T15:30:10",
        ),
    ),
    (
        dict(
            _datetime=datetime.datetime(2022, 8, 31, 9, 45, 25),
            _format=DateTimeFormat.RFC3339,
        ),
        dict(
            result="2022-08-31 09:45:25",
        ),
    ),
    (
        dict(
            _datetime=datetime.datetime(2022, 5, 29, 22, 15, 5),
            _format=f"%Y_%m_%d %H:%M:%S%z",
        ),
        dict(
            result="2022_05_29 22:15:05",
        ),
    ),
]


# endregion: PyTest parametrized variables


class TestDateTimeOps:
    @pytest.mark.parametrize("payload, expect", export_datetime_happy)
    def test_happy_export_datetime(self, payload, expect):
        result = export_datetime(**payload)

        assert result == expect["result"]
