from pymongo import MongoClient

# helper function to connect with mongodb and return connection object
def connect_db(app):
    return MongoClient(app.config['DB_HOST'], app.config['DB_PORT'])

