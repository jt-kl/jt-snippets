import datetime
import unittest.mock

import pytest
from jt_snippets.datetime_ops import DateTimeFormat, export_datetime, get_weekdays, get_weekends

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

get_weekends_happy = [
    (
        dict(
            ranges=(
                datetime.datetime(2022, 9, 7),
                datetime.datetime(2022, 10, 1),
            )
        ),
        dict(
            result=[
                datetime.datetime(2022, 9, 10),
                datetime.datetime(2022, 9, 11),
                datetime.datetime(2022, 9, 17),
                datetime.datetime(2022, 9, 18),
                datetime.datetime(2022, 9, 24),
                datetime.datetime(2022, 9, 25),
            ]
        ),
    )
]
get_weekends_sad = []


get_weekdays_happy = [
    (
        dict(
            ranges=(
                datetime.datetime(2022, 9, 7),
                datetime.datetime(2022, 10, 1),
            )
        ),
        dict(
            result=[
                datetime.datetime(2022, 9, 7),
                datetime.datetime(2022, 9, 8),
                datetime.datetime(2022, 9, 9),
                datetime.datetime(2022, 9, 12),
                datetime.datetime(2022, 9, 13),
                datetime.datetime(2022, 9, 14),
                datetime.datetime(2022, 9, 15),
                datetime.datetime(2022, 9, 16),
                datetime.datetime(2022, 9, 19),
                datetime.datetime(2022, 9, 20),
                datetime.datetime(2022, 9, 21),
                datetime.datetime(2022, 9, 22),
                datetime.datetime(2022, 9, 23),
                datetime.datetime(2022, 9, 26),
                datetime.datetime(2022, 9, 27),
                datetime.datetime(2022, 9, 28),
                datetime.datetime(2022, 9, 29),
                datetime.datetime(2022, 9, 30),
            ]
        ),
    ),
]
get_weekends_sad = []


# endregion: PyTest parametrized variables


class TestDateTimeOps:
    @pytest.mark.parametrize("payload, expect", export_datetime_happy)
    def test_happy_export_datetime(self, payload, expect):
        result = export_datetime(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", get_weekends_happy)
    def test_happy_get_weekends(self, payload, expect):
        result = get_weekends(**payload)

        assert len(result) == len(expect["result"])
        for index, item in enumerate(result):
            assert item == expect["result"][index]

    @pytest.mark.parametrize("payload, expect", get_weekdays_happy)
    def test_happy_get_weekdays(self, payload, expect):
        result = get_weekdays(**payload)

        assert len(result) == len(expect["result"])
        for index, item in enumerate(result):
            assert item == expect["result"][index]
