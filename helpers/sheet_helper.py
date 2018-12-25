import pyexcel as pe
import os
from flask import current_app

def file_to_records(filename, config):
  filePath = os.path.join(config['UPLOAD_FOLDER'], filename)
  sheet = pe.get_sheet(file_name=filePath, name_columns_by_row=0)
  records = sheet.to_records()
  totalRows = sheet.number_of_rows()
  return records, totalRows