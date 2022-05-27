import cProfile
import pstats
import io


# def profile(fnc):

#     def inner(*args, **kwargs):

#         pr = cProfile.Profile()
#         pr.enable()
#         retval = fnc(*args, **kwargs)
#         pr.disable()
#         s = io.StringIO()
#         sortby = 'cumulative'
#         ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#         ps.print_stats()
#         print(s.getvalue())
#         return retval

#     return inner


# @profile
def code_to_profile():
    from xmlrpc.client import boolean
    from pymongo_db import main
    import pandas as pd
    from cerberus import Validator
    from loguru import logger
    try:
        db = main.get_database()
        users_collection = db["users"]
        v = Validator()

        load_dict = pd.read_csv('pymongo/accounts.csv')  # "accounts.csv"
        load_dict.columns = load_dict.columns.str.lower()
        load_dict = load_dict.to_dict(orient="records")
        if (temp := main.validate_load_users(load_dict)) is not True:
            print("This .csv has failed validation. Please try again.")
            return False
        users_collection.insert_many(load_dict)
        return load_dict
    except FileNotFoundError:
        logger.exception("NEW EXCEPTION")
        return False


with cProfile.Profile() as pr:
    code_to_profile()
pr.print_stats()
