# Config class for setting the config of app
class Config(object):
    DB_HOST = "localhost"
    DB_PORT = 27017
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    UPLOAD_FOLDER = '/Users/aditya/development/assignments/excel-upload-backend/uploads'