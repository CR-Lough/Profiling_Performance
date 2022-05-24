"""
Classes for user information for the social network project
"""
# pylint: disable=R0903
from pprint import pprint
import main
from loguru import logger

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)


class UserCollection:
    """
    Contains methods to interact with the UserTable in twitter.db
    """

    @logger.catch(message="error in UserCollection __init__")
    def __init__(self):
        self.database = {}

    @logger.catch(message="error in UserCollection.add_user() method")
    def add_user(self, user_id: str, email: str, user_name: str, user_lastname: str):
        """
        Adds a new user to the database
        """
        try:
            db = main.get_database()
            db.users.insert_one(
                {
                    "user_id": user_id,
                    "name": user_name,
                    "lastname": user_lastname,
                    "email": email,
                },
            )
            return True
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserCollection.modify_user() method")
    def modify_user(self, user_id: str, email: str, user_name: str, user_lastname: str):
        """
        Modifies an existing user
        """
        try:
            db = main.get_database()
            row = db.users.find_one({"user_id": user_id})
            print("Found document:")
            pprint(row)
            result = db.users.replace_one(
                {"_id": row.get("_id")},
                {
                    "user_id": user_id,
                    "name": user_name,
                    "lastname": user_lastname,
                    "email": email,
                },
            )
            print("document updated to:")
            result = db.users.find_one({"user_id": user_id})
            pprint(result)
            return result
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserCollection.delete_user() method")
    def delete_user(self, user_id: str):
        """
        Deletes an existing user
        """
        try:
            db = main.get_database()
            row = db.users.find_one({"user_id": user_id})
            db.users.delete_one(row)

            print("Deleted document:")
            pprint(row)
            return row
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserCollection.search_user() method")
    def search_user(self, user_id: str):
        """
        Searches for user data
        """
        try:
            db = main.get_database()
            row = db.users.find_one({"user_id": user_id})
            return row
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False
