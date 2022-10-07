import unittest.mock

import pytest
from jt_snippets.validator_ops import validate_count_range

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
validate_count_range_happy = [
    (
        dict(
            _value=10,
            lower_bound=5,
            upper_bound=20,
        ),
        dict(
            result=True,
        ),
    ),
    (
        dict(
            _value=20,
            lower_bound=10,
            upper_bound=20,
        ),
        dict(
            result=False,
        ),
    ),
    (
        dict(
            _value=-10,
            lower_bound=-20,
            upper_bound=50,
        ),
        dict(
            result=True,
        ),
    ),
]
validate_count_range_sad = [
    (
        dict(
            _value=120,
            lower_bound=130,
            upper_bound=110,
        ),
        dict(
            result=None,
            exception_type=ValueError,
            exception_message=(
                f"Value of lower bound range cannot be greater " f"than or equal to value of upper bound range"
            ),
        ),
    ),
    (
        dict(
            _value=-20,
            lower_bound=-15,
            upper_bound=-25,
        ),
        dict(
            result=None,
            exception_type=ValueError,
            exception_message=(
                f"Value of lower bound range cannot be greater " f"than or equal to value of upper bound range"
            ),
        ),
    ),
]

# endregion: PyTest parametrized variables


class TestValidatorOps:
    @pytest.mark.parametrize("payload, expect", validate_count_range_happy)
    def test_happy_validate_count_range(self, payload, expect):
        result = validate_count_range(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", validate_count_range_sad)
    def test_sad_validate_count_range(self, payload, expect):
        with pytest.raises(expect["exception_type"], match=expect["exception_message"]):
            result = validate_count_range(**payload)
