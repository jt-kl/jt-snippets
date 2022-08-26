import csv
import pathlib
import shutil
import tempfile

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


if __name__ == "__main__":
    update_csv_file(SOURCE_FILE, FIELDS, True)
