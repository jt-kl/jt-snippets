import csv
import pathlib
import random

import faker


def generate_people_data(
    # path: pathlib.Path,
    count: int = 100,
):
    """
    Generate a collection of person data and output as a CSV file

    Args:
        path: Storage path for CSV file
        count: Total required records

    Remarks;
        Attributes that would be generated will be as such:
        - First name
        - Last name
        - Email Address
        - Age
        - Address Line 1
        - Address Line 2
        - City
        - State
        - Postal Code
        - Country
        - Mobile Number

    """
    f = faker.Faker()

    for i in range(count):
        _first_name = f.first_name()
        _last_name = f.last_name()

        entry = dict(
            first_name=_first_name,
            last_name=_last_name,
            email_address=f"{_first_name.lower()}.{_last_name.lower()}@acme.com",
            age=random.randrange(18, 55),
            address_line_1=f.building_number(),
            address_line_2=f"{f.street_name()} {f.street_suffix()}",
            city=f.city(),
            state=f.country_code(),
            postal_code=f.postcode(),
            country="United States",
            mobile_number=f.phone_number(),
        )

        print(entry)

        fields = [
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


if __name__ == "__main__":
    generate_people_data()
