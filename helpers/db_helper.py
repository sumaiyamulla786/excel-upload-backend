from pymongo import MongoClient
from flask import g

# helper function to connect with mongodb and return connection object
def connect_db(app):
    return MongoClient(app.config['DB_HOST'], app.config['DB_PORT'])

def insert_record(record):
    db = g.db.testData
    collection = db.sales
    salesRecord = {}
    keys = record.keys()
    for key in keys:
        salesRecord[key] = record[key]
    collection.insert_one(document=salesRecord, bypass_document_validation=True)
