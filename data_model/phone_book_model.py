from datetime import datetime
from config.dev import Base
import sqlalchemy as sqla


"""Data Model of Phone Book Table"""
class PhoneBook(Base):
    __tablename__ = "phonebook"
    _id = sqla.Column(sqla.Integer, primary_key=True)
    sur_name = sqla.Column(sqla.String(32))
    first_name = sqla.Column(sqla.String(32))
    phone_number = sqla.Column(sqla.Integer)
    creationDate = sqla.Column(
        sqla.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    updatedDate = sqla.Column(
        sqla.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    address = sqla.Column(sqla.String(255))

