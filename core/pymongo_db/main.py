"""
main driver for a simple social network project
"""
from xmlrpc.client import boolean
from pymongo_db import users
from pymongo_db import user_status
from pymongo_db import menu
import pandas as pd
from cerberus import Validator
from loguru import logger
import time

logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)


def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    user = users.UserCollection()
    return user


def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    status = user_status.UserStatusCollection()
    return status


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = (
        "mongodb+srv://crlough:wakaflocka@cluster0.cqd6b.mongodb.net/homework5db"
    )

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient

    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["hw_db"]

def drop_database():
    db = get_database()
    col = db["users"]
    col.drop()
    col = db["status_updates"]
    col.drop()

def load_users(filename: str):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    try:
        db = get_database()
        users_collection = db["users"]

        load_dict = pd.read_csv(filename)  # "accounts.csv"
        load_dict.columns = load_dict.columns.str.lower()
        load_dict = load_dict.to_dict(orient="records")
        users_collection.insert_many(load_dict)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.info(f"PyMongo ran 'load_users()' in {run_time:.4f} secs")
        return load_dict
    except FileNotFoundError:
        logger.exception("NEW EXCEPTION")
        return False


def load_statuses(filename: str):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    try:
        db = get_database()
        status_collection = db["status_updates"]

        load_dict = pd.read_csv(filename)  # "status_updates.csv"
        load_dict.columns = load_dict.columns.str.lower()
        load_dict = load_dict.to_dict(orient="records")
        status_collection.insert_many(load_dict)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.info(f"PyMongo ran 'load_statuses()' in {run_time:.4f} secs")
        return load_dict
    except FileNotFoundError:
        logger.exception("NEW EXCEPTION")
        return False


def add_user(
    user_id: str,
    email: str,
    user_name: str,
    user_lastname: str,
    user_collection: object,
):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    new_user = user_collection.add_user(
        user_id, email, user_name, user_lastname)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'add_user()' in {run_time:.4f} secs")
    return new_user


def update_user(
    user_id: str,
    email: str,
    user_name: str,
    user_lastname: str,
    user_collection: object,
):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    updated_user = user_collection.modify_user(
        user_id, email, user_name, user_lastname)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'update_user()' in {run_time:.4f} secs")
    return updated_user


def delete_user(user_id: str, user_collection: object):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    purge_id = user_collection.delete_user(user_id)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'delete_user()' in {run_time:.4f} secs")
    return purge_id


def search_user(user_id: str, user_collection: object):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    start_time = time.perf_counter()
    find_user = user_collection.search_user(user_id)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'search_user()' in {run_time:.4f} secs")
    return find_user


def add_status(
    user_id: str, status_id: str, status_text: str, status_collection: object
):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    new_status = status_collection.add_status(user_id, status_id, status_text)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'add_status()' in {run_time:.4f} secs")
    return new_status


def update_status(
    status_id: str, user_id: str, status_text: str, status_collection: object
):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    modify_status = status_collection.modify_status(
        user_id, status_id, status_text)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'update_status()' in {run_time:.4f} secs")
    return modify_status


def delete_status(status_id: str, status_collection: object):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    start_time = time.perf_counter()
    purge_id = status_collection.delete_status(status_id)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'delete_status()' in {run_time:.4f} secs")
    return purge_id


def search_status(status_id: str, status_collection: object):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    # query = (socialnetwork_model.StatusTable
    #      .select(socialnetwork_model.StatusTable)
    #      .where(socialnetwork_model.StatusTable.status_id == status_id))
    start_time = time.perf_counter()
    find_status = status_collection.search_status(status_id)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"PyMongo ran 'search_status()' in {run_time:.4f} secs")
    return find_status