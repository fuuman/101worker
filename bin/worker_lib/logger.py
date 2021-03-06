import os
import datetime
try:
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)
    db = client['worker']

    MONGODB_USER = os.environ.get('MONGODB_USER', '')
    MONGODB_PWD = os.environ.get('MONGODB_PWD', '')

    if MONGODB_USER and MONGODB_PWD:
        db.authenticate(MONGODB_USER, MONGODB_PWD)

    MONGO = True
except ImportError:
    MONGO = False
    print('pymongo is missing: "pip install pymongo"')

def report_error(error_type, error_data):
    '''
    Logs an error to an internal dump.
    :param error_type: error name
    :param error_data: data for the error, e.g. stack trace
    '''

    print(error_type)
    print(error_data)

    if MONGO:
        db.errors.insert_one({
            'error': error_type,
            'data': error_data,
            'created_at': datetime.datetime.now()
        })
