from flask import request, Blueprint, jsonify
import pyexcel as pe
from helpers.db_helper import insert_record

file_upload = Blueprint('file_upload', __name__)

@file_upload.route('/upload', methods=['POST'])
def upload():
    filename = request.files['excel'].filename
    extension = filename.split('.')[-1]
    content = request.files['excel'].read()
    sheet = pe.get_sheet(file_type=extension, file_content=content, name_columns_by_row=0)
    records = sheet.to_records()
    for record in records:
        insert_record(record)
    return jsonify({"result": sheet.dict})