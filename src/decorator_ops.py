import functools
import time
import typing


def exponential_backoff(
    func: typing.Callable,
    attempts: int = 5,
):
    """
    Function decorator to handle retry attempts on an exponential backoff basis.

    Args:
        func: Wrapped function
        attempts: Maximum callback attempts
    """

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        for attempt in range(1, attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception:
                duration = 15 + (attempt * 15)
                time.sleep(duration)
                continue

    return func_wrapper


def code_execution_timer(
    func: typing.Callable,
):
    """
    Function decorator to calculate execution duration of code block.

    Args:
        func: Wrapped function
    """

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Elapsed duration: {duration} milliseconds")

        return result

    return func_wrapper
