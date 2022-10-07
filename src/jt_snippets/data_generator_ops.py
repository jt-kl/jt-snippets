import random

import faker


def generate_people_data(
    count: int = 10,
):
    """
    Generate a collection of person data

    Args:
        count: Total required records

    Examples:
        generate_people_data()
        generate_people_data(count=20)

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

    records = []

    for i in range(count):
        _first_name = f.first_name()
        _last_name = f.last_name()

        records.append(
            dict(
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
        )
