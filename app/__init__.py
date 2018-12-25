from flask import Flask
from flask_cors import CORS
from helpers.config import Config
from celery import Celery

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  celery.conf.update(app.config)
  CORS(app)
  return app