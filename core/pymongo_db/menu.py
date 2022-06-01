"""
Provides a basic frontend
"""
import os
import sys

from pymongo_db import main
from peewee import *
from cerberus import Validator
from loguru import logger
from pprint import pprint
import pysnooper

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)


@pysnooper.snoop()
def load_users():
    """
    Loads user accounts from a file
    """
    filename = 'accounts.csv'#input("Enter filename of user file: ")
    main.load_users(filename)


@pysnooper.snoop()
def load_status_updates():
    """
    Loads status updates from a file
    """
    filename = 'status_updates.csv'#input("Enter filename for status file: ")
    main.load_statuses(filename)


@pysnooper.snoop()
def add_user():
    """
    Adds a new user into the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    user_schema = _user_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   user_schema) is False
    ):
        print(v.errors)
    while v.validate({"email": (email := 'connor')}, user_schema) is False:
        print(v.errors)
    while (
        v.validate({"name": (user_name := 'connor')},
                   user_schema) is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"lastname": (user_lastname := 'connor')}, user_schema
        )
        is False
    ):
        print(v.errors)
    if not main.add_user(user_id, email, user_name, user_lastname, user_collection):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


@pysnooper.snoop()
def update_user():
    """
    Updates information for an existing user
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    user_schema = _user_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   user_schema) is False
    ):
        print(v.errors)
    while v.validate({"email": (email := 'connor')}, user_schema) is False:
        print(v.errors)
    while (
        v.validate({"name": (user_name := 'connor')},
                   user_schema) is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"lastname": (user_lastname := 'connor')}, user_schema
        )
        is False
    ):
        print(v.errors)
    # try:
    if not main.update_user(user_id, email, user_name, user_lastname, user_collection):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")
    # except TypeError:
    #   logger.exception("NEW EXCEPTION")
    #   pass


@pysnooper.snoop()
def search_user():
    """
    Searches a user in the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    user_schema = _user_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   user_schema) is False
    ):
        print(v.errors)
    result = main.search_user(user_id, user_collection)
    #   try:
    if not result:
        print("ERROR: User does not exist")
    else:
        pprint(result)
    # except AttributeError:
    #     logger.exception("NEW EXCEPTION")
    #     pass


@pysnooper.snoop()
def delete_user():
    """
    Deletes user from the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    user_schema = _user_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   user_schema) is False
    ):

        print(v.errors)
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


@pysnooper.snoop()
def add_status():
    """
    Adds a new status into the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    status_schema = _status_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   status_schema) is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"status_id": (status_id := 'connor')}, status_schema)
        is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"status_text": (status_text := 'connor')}, status_schema
        )
        is False
    ):
        print(v.errors)
    if not main.add_status(user_id, status_id, status_text, status_collection):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


@pysnooper.snoop()
def update_status():
    """
    Updates information for an existing status
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    status_schema = _status_schema()
    while (
        v.validate({"user_id": (user_id := 'connor')},
                   status_schema) is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"status_id": (status_id := 'connor')}, status_schema)
        is False
    ):
        print(v.errors)
    while (
        v.validate(
            {"status_text": (status_text := 'connor')}, status_schema
        )
        is False
    ):
        print(v.errors)
    if not main.update_status(status_id, user_id, status_text, status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


@pysnooper.snoop()
def search_status():
    """
    Searches a status in the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    status_schema = _status_schema()
    while (
        v.validate(
            {"status_id": (status_id := 'connor')},
            status_schema,
        )
        is False
    ):
        print(v.errors)
    result = main.search_status(status_id, status_collection)
    if not result:
        print("ERROR: Status does not exist")
    else:
        pprint(result)


@pysnooper.snoop()
def delete_status():
    """
    Deletes status from the database
    """
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    v = Validator()
    status_schema = _status_schema()
    while (
        v.validate(
            {"status_id": (status_id := 'connor')},
            status_schema,
        )
        is False
    ):
        print(v.errors)
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


@pysnooper.snoop()
def _user_schema():
    _user_schema = {
        "user_id": {
            "type": "string",
            "min": 1,
            "max": 999,
            "empty": False,
        },
        "name": {"type": "string", "minlength": 1, "maxlength": 100, "empty": False},
        "lastname": {
            "type": "string",
            "minlength": 1,
            "maxlength": 100,
            "empty": False,
        },
        "email": {
            "type": "string",
            "minlength": 1,
            "maxlength": 100,
            "empty": False,
        },
    }
    return _user_schema


@pysnooper.snoop()
def _status_schema():
    _status_schema = {
        "status_id": {
            "type": "string",
            "min": 1,
            "max": 999,
            "empty": False,
        },
        "user_id": {
            "type": "string",
            "minlength": 1,
            "maxlength": 50,
            "empty": False,
        },
        "status_text": {
            "type": "string",
            "minlength": 1,
            "maxlength": 100,
            "empty": False,
        },
    }
    return _status_schema


@pysnooper.snoop()
def quit_program():
    """
    Quits program
    """
    sys.exit()

def setup():
        main.drop_database()
        v = Validator()
        user_collection = main.init_user_collection()
        status_collection = main.init_status_collection()

with logger.catch(message="Because we never know..."):
    if __name__ == "__main__":
        main.drop_database()
        v = Validator()
        user_collection = main.init_user_collection()
        status_collection = main.init_status_collection()
        menu_options = {
            "A": load_users,
            "B": load_status_updates,
            "C": add_user,
            "D": update_user,
            "E": search_user,
            "F": delete_user,
            "G": add_status,
            "H": update_status,
            "I": search_status,
            "J": delete_status,
            "Q": quit_program,
        }
        while True:
            user_selection = input(
                """
                                A: Load user database
                                B: Load status database
                                C: Add user
                                D: Update user
                                E: Search user
                                F: Delete user
                                G: Add status
                                H: Update status
                                I: Search status
                                J: Delete status
                                Q: Quit

                                Please enter your choice: """
            )
            if user_selection.upper() in menu_options:
                try:
                    menu_options[user_selection.upper()]()
                except KeyError:
                    logger.exception("NEW EXCEPTION")
            else:
                print("Invalid option")
