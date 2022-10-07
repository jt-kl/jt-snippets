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
