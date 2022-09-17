def validate_count_range(
    _value: int,
    lower_bound: int = 0,
    upper_bound: int = 0,
) -> bool:
    """
    Validates value is between specified ranges

    Args:
        _value: Value to be validated
        lower_bound: Acceptable lower bound range of value
        upper_bound: Acceptable upper bound range of value
    """
    assert not lower_bound >= upper_bound, (
        f"Value of lower bound range cannot be greater "
        f"than or equal to value of upper bound range"
    )

    return lower_bound < _value < upper_bound
