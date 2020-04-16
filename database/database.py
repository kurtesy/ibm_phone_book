import os
from config.dev import db, meta, session, Base, DB_NAME
from data_model.phone_book_model import PhoneBook

# Data to initialize database with
TEST_DATA = [
    {"_id": 1, "sur_name": "Patel", "first_name": "Nishant", "phone_number": 1234567890, "address": "Hyderabad"},
    {"_id": 2, "sur_name": "abc", "first_name": "xyz", "phone_number": 9876543210, "address": "Hyderabad"},
    {"_id": 3, "sur_name": "Prasad", "first_name": "Ram", "phone_number": 9999999999, "address": "Hyderabad"}
]


def main():
    # Delete database file if it exists currently
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    # Create the database
    meta.create_all(db)

    # Create All Tables
    Base.metadata.create_all(db)

    # iterate over the PEOPLE structure and populate the database
    for data in TEST_DATA:
        p = PhoneBook(_id=data["_id"] ,sur_name=data["sur_name"], first_name=data["first_name"],
                      phone_number=data["phone_number"], address=data["address"])
        session.add(p)
        session.commit()