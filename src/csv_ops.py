import csv
import pathlib
import shutil
import tempfile
import typing

BASE_DIRECTORY = pathlib.Path(__file__).parent
SOURCE_FILE = BASE_DIRECTORY.joinpath("test.csv")
DESTINATION_DIRECTORY = BASE_DIRECTORY.joinpath("output.csv")

# endregion: Pre-flight operations
TEMP_FILE = tempfile.NamedTemporaryFile(mode="w", delete=True)
FIELDS = [
    "first_name",
    "last_name",
    "email_address",
    "age",
    "address_line_1",
    "address_line_2",
    "city",
    "state",
    "postal_code",
    "country",
    "mobile_number",
]


def update_csv_file(
    source: pathlib.Path,
    fields: list[str],
    header: bool = False,
):
    """
    Updates content of a CSV file

    Args:
        source: Source CSV file
        fields: Source CSV header fields
        header: Source CSV contains header
    """
    temp_file = tempfile.NamedTemporaryFile(mode="w", delete=True)

    with open(source, "r") as csv_file, temp_file:
        reader = csv.DictReader(csv_file, fieldnames=fields)
        writer = csv.DictWriter(temp_file, fieldnames=fields)
        writer.writeheader()

        # Skips first/header row
        if header:
            next(reader)

        for row in reader:
            entry = dict()

            # Perform row data checks and/or manipulations
            for key, value in row.items():
                if row["first_name"] == "Abigail":
                    row["first_name"] = "Sarah"

                entry[key] = value

            if entry:
                writer.writerow(entry)

        shutil.copy(pathlib.Path(TEMP_FILE.name), DESTINATION_DIRECTORY)


def read_csv_file(
    path: pathlib.Path,
    header: bool = False,
    delimiter: str = ",",
    **kwargs,
) -> typing.Iterator:
    """Read CSV file.

    Args:
        path: Path to CSV file
        header: Skip header row
        delimiter: Record delimiter
    """
    with open(path, "r") as file:
        reader = csv.DictReader(file, delimiter=delimiter, **kwargs)

        if not header:
            yield from reader

        # Skips the CSV header row
        next(reader)

        yield from reader


def write_csv_file(
    path: pathlib.Path,
    field_names: list,
    rows: typing.Union[list[dict], typing.Iterator[dict]],
    header: bool = True,
    **kwargs,
):
    """
    Write CSV file.

    Args:
        path: Path to CSV file
        field_names: Field names
        rows: Rows of data to be written
        header: Write header row
    """
    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_names, **kwargs)

        if header:
            writer.writeheader()

        for row in rows:
            writer.writerow(row)
