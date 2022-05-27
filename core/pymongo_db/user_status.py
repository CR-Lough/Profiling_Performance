"""
classes to manage the user status messages
"""
# pylint: disable=R0903
from pprint import pprint
from pymongo_db import main
from loguru import logger

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)


class UserStatusCollection:
    """
    Contains methods to interact with the StatusTable in twitter.db
    """

    @logger.catch(message="error in UserStatusCollection __init__")
    def __init__(self):
        self.database = {}

    @logger.catch(message="error in UserStatusCollection.add_status() method")
    def add_status(self, status_id: str, user_id: str, status_text: str):
        """
        add a new status message to the database
        """
        try:
            db = main.get_database()
            db.status_updates.insert_one(
                {
                    "status_id": status_id,
                    "user_id": user_id,
                    "status_text": status_text,
                },
            )
            return True
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.modify_status() method")
    def modify_status(self, status_id: str, user_id: str, status_text: str):
        """
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        """
        try:
            db = main.get_database()
            row = db.status_updates.find_one({"status_id": status_id})
            print("Found document:")
            pprint(row)
            result = db.status_updates.replace_one(
                {"_id": row.get("_id")},
                {
                    "status_id": status_id,
                    "user_id": user_id,
                    "status_text": status_text,
                },
            )
            print("document updated to:")
            result = db.status_updates.find_one({"status_id": status_id})
            pprint(result)
            return result
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.delete_status() method")
    def delete_status(self, status_id: str):
        """
        deletes the status message with id, status_id
        """
        try:
            db = main.get_database()
            row = db.status_updates.find_one({"status_id": status_id})
            db.status_updates.delete_one(row)

            print("Deleted document:")
            pprint(row)
            return row
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False

    @logger.catch(message="error in UserStatusCollection.search_status() method")
    def search_status(self, status_id: str):
        """
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        """
        try:
            db = main.get_database()
            row = db.status_updates.find_one({"status_id": status_id})
            return row
        except NameError:
            logger.exception("NEW EXCEPTION")
            return False
