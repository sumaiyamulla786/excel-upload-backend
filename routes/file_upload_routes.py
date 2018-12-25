from flask import request, Blueprint, jsonify, current_app
import pyexcel as pe
from helpers.celery_helper import insert_documents
from pymongo.errors import DuplicateKeyError
from werkzeug.utils import secure_filename
import os

file_upload = Blueprint('file_upload', __name__)

@file_upload.route('/upload', methods=['POST'])
def upload():
    excelFile = request.files['excel']
    filename = excelFile.filename
    filename = secure_filename(filename)
    extension = filename.split('.')[-1]
    excelFile.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    task = insert_documents.delay(filename)
    return jsonify({ 'task': task.id })