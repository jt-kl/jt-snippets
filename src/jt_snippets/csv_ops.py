import shutil
from csv import DictReader, DictWriter
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterator, Union


def update_csv_file(
    path: Path,
    fields: list[str],
    records: Union[list[dict], Iterator[dict]],
    header: bool = False,
):
    """
    Updates content of a CSV file

    Args:
        path: Source CSV file
        fields: Source CSV header fields
        records: Collection of replacement records
        header: Source CSV contains header
    """
    temp_file = NamedTemporaryFile(mode="w", delete=True)

    with open(path, "r") as csv_file, temp_file:
        reader = DictReader(csv_file, fieldnames=fields)
        writer = DictWriter(temp_file, fieldnames=fields)
        writer.writeheader()

        # Skips first/header row
        if header:
            next(reader)

        for record in records:
            for key, (original, replacement) in record.items():

                for row in reader:
                    entry = dict()

                    # Perform row data checks and/or manipulations
                    for _key, _value in row.items():
                        if _key == key and _value == original:
                            entry[key] = replacement
                        else:
                            entry[key] = _value

                    if entry:
                        writer.writerow(entry)

        shutil.copy(Path(temp_file.name), path)


def read_csv_file(
    path: Path,
    header: bool = False,
    delimiter: str = ",",
    **kwargs,
) -> Iterator:
    """
    Read CSV file.

    Args:
        path: Path to CSV file
        header: Skip header row
        delimiter: Record delimiter
    """
    with open(path, "r") as file:
        reader = DictReader(
            file,
            delimiter=delimiter,
            **kwargs,
        )

        if not header:
            yield from reader

        # Skips the CSV header row
        next(reader)

        yield from reader


def write_csv_file(
    path: Path,
    field_names: list,
    rows: Union[list[dict], Iterator[dict]],
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
        writer = DictWriter(
            file,
            fieldnames=field_names,
            **kwargs,
        )

        if header:
            writer.writeheader()

        for row in rows:
            writer.writerow(row)
