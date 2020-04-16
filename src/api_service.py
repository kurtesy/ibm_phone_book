"""
This is the main API module and supports all the REST actions for the phonebook data
"""
import json
from flask import make_response, abort, Flask, jsonify, request
from sqlalchemy import update
from config.dev import db, session
from data_model.phone_book_model import PhoneBook

server = Flask(__name__)

@server.route('/')
def home():
    return "IBM!! Server is Running"

@server.route('/api/phonebook', methods=['GET'])
def list_all():
    """
    This function responds to a request for /api/phonebook
    with the complete lists of people
    :return:        json string of list of people
    """
    phoneList = session.query(PhoneBook).all()
    session.close()
    data = jsonify([as_dict(entry) for entry in phoneList])
    return data

@server.route('/api/phonebook/search/<sur_name>', methods=['GET'])
def get_data(sur_name):
    """
    This function responds to a request for /api/people/{PhoneBook_id}
    with one matching PhoneBook from people
    :param sur_name:   sur_name of entry to find
    :return:           PhoneBook matching id
    """
    phonebook = session.query(PhoneBook).filter(PhoneBook.sur_name == sur_name).one_or_none()
    session.close()
    if phonebook:
        data = jsonify(as_dict(phonebook))
        return data
    else:
        abort(
            404,
            "PhoneBook Entry not found for Surname: {sur_name}".format(sur_name=sur_name),
        )

@server.route('/api/phonebook/add', methods=['POST'])
def create():
    """
    This function creates a new PhoneBook in the people structure
    based on the passed in PhoneBook data
    :param phonebook:  PhoneBook to create in people structure
    :return:        201 on success, 406 on PhoneBook exists
    """
    args = request.args
    required_args = ['sur_name', 'first_name', 'phone_number']
    for arg in required_args:
        if not arg in args:
            abort(404,"Parameter {param} is missing".format(param=arg))
    sur_name = args.get("sur_name")
    first_name = args.get("first_name")
    phone_number = args.get("phone_number")
    address = 'NA'
    if 'address' in args:
        address = args.get("address")

    existing_entry = (
        session.query(PhoneBook).filter(PhoneBook.first_name == first_name)
        .filter(PhoneBook.sur_name == sur_name)
        .one_or_none()
    )

    if not existing_entry:
        phonebook = PhoneBook(sur_name=sur_name, first_name=first_name,
                      phone_number=phone_number, address=address)
        session.add(phonebook)
        session.commit()
        session.close()

        data = jsonify(as_dict(phonebook))
        return data, 201

    else:
        abort(
            409,
            "Entry {first_name} {sur_name} exists already".format(
                sur_name=sur_name, first_name=first_name
            ),
        )

@server.route('/api/phonebook/update/<sur_name>/<first_name>', methods=['PUT'])
def update(sur_name, first_name):
    """
    This function updates an existing PhoneBook in the people structure
    Throws an error if a PhoneBook with the name we want to update to
    already exists in the database.
    :param sur_name:   sur_name of the  entry to update in the people structure
    :param first_name:   first_name of the  entry to update in the people structure
    :param phonebook:      phonebook to update
    :return:            updated phonebook structure
    """
    update_phonebook = session.query(PhoneBook).filter(PhoneBook.first_name == first_name)\
        .filter(PhoneBook.sur_name == sur_name).one_or_none()

    if not update_phonebook:
        abort(
            404,
            "Entry {first_name} {sur_name} does not exist".format(
                sur_name=sur_name, first_name=first_name
            ),
        )

    else:
        args = request.args
        sur_name = args.get("sur_name", update_phonebook.sur_name)
        first_name = args.get("first_name", update_phonebook.first_name)
        phone_number = args.get("phone_number", update_phonebook.phone_number)
        address = args.get("address", update_phonebook.address)
        updatedObject = update({PhoneBook.sur_name: sur_name,
                                PhoneBook.first_name:first_name,
                                PhoneBook.phone_number:phone_number,
                                PhoneBook.address:address})
        session.commit()
        session.close()
        data = jsonify(as_dict(updatedObject))
        return data, 200


def delete(sur_name, first_name):
    """
    This function deletes a Entry from the PhoneBook structure
    :param sur_name:   sur_name of the entry in PhoneBook to delete
    :param first_name:   first_name of the entry in PhoneBook to delete
    :return:            200 on successful delete, 404 if not found
    """
    entry = session.query(PhoneBook).filter(PhoneBook.first_name == first_name)\
        .filter(PhoneBook.sur_name == sur_name).one_or_none()

    if entry is not None:
        db.session.delete(entry)
        db.session.commit()
        return jsonify(
            "PhoneBook entry for {sur_name} {first_name} deleted".format(sur_name=sur_name, first_name=first_name)), 200
    else:
        abort(
            404,
            "PhoneBook entry for {sur_name} {first_name} deleted".format(sur_name=sur_name, first_name=first_name),
        )

def as_dict(data):
    return {c.name: getattr(data, c.name) for c in data.__table__.columns}

"""Starts the server"""
def run():
    server.run(debug=True)
