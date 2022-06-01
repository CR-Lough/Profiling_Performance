import cProfile
import pstats
import io
import os
import functools
import time
import pymongo_db
from loguru import logger
import sqlite_db

from pymongo_db import menu, main
from sqlite_db import menu, main


if __name__ == "__main__":
    os.remove('out_2022.06.01.log')
    logger.add("out_{time:YYYY.MM.DD}.log", backtrace=True, diagnose=True)
    user_collection = pymongo_db.main.init_user_collection()
    status_collection = pymongo_db.main.init_status_collection()
    sqlite_db.menu.setup()
    pymongo_db.menu.setup()
    
    pymongo_db.menu.load_users()   
    sqlite_db.menu.load_users()
    pymongo_db.menu.add_user()
    sqlite_db.menu.add_user()
    pymongo_db.menu.search_user()
    sqlite_db.menu.search_user()
    pymongo_db.menu.update_user()
    sqlite_db.menu.update_user()
    pymongo_db.menu.delete_user()
    sqlite_db.menu.delete_user()

    pymongo_db.menu.load_status_updates()   
    sqlite_db.menu.load_status_updates()
    pymongo_db.menu.add_status()
    sqlite_db.menu.add_status()
    pymongo_db.menu.search_status()
    sqlite_db.menu.search_status()
    pymongo_db.menu.update_status()
    sqlite_db.menu.update_status()
    pymongo_db.menu.delete_status()
    sqlite_db.menu.delete_status()


# # @profile
# def code_to_profile():
#     from xmlrpc.client import boolean
#     from pymongo_db import main
#     import pandas as pd
#     from cerberus import Validator
#     from loguru import logger
#     try:
#         db = main.get_database()
#         users_collection = db["users"]
#         v = Validator()

#         load_dict = pd.read_csv('pymongo/accounts.csv')  # "accounts.csv"
#         load_dict.columns = load_dict.columns.str.lower()
#         load_dict = load_dict.to_dict(orient="records")
#         if (temp := main.validate_load_users(load_dict)) is not True:
#             print("This .csv has failed validation. Please try again.")
#             return False
#         users_collection.insert_many(load_dict)
#         return load_dict
#     except FileNotFoundError:
#         logger.exception("NEW EXCEPTION")
#         return False


# with cProfile.Profile() as pr:
#     code_to_profile()
# pr.print_stats()
