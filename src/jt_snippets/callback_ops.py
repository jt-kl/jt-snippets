import time
from functools import wraps


def execution_timer():
    """
    Function decorator to calculate runtime duration of a method/function.
    """

    def log_wrapper(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            duration = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Total Runtime: {duration}")

            return result

        return func_wrapper

    return log_wrapper


def progress_bar_callback(
    size: int,
    completed: int,
):
    """
    Progress bar callback function

    Args:
        size: Total task size
        completed: Completed task size
    """
    width = 20
    multiplier = 100 / width

    percentage = 100 * (completed / float(size))
    remaining = "." * (width - int(percentage / multiplier))
    progress = "#" * int(percentage / multiplier)

    bar = f"{progress}{remaining}"

    if completed < size:
        print(f"|{bar}| {percentage:.2f}%", end="\r")
    else:
        print(f"|{bar}| {percentage:.2f}%")


def progress_text_callback(
    size: int,
    completed: int,
):
    """
    Progress text callback function

    Args:
        size: Total task size
        completed: Completed task size
    """
    percentage = 100 * (completed / float(size))

    if completed < size:
        print(f"{percentage:.2f}%\r")
    else:
        print(f"{percentage:.2f}%\n")
