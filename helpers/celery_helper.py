from app import celery
from helpers.db_helper import insert_record
from helpers.sheet_helper import file_to_records
import time
from app import create_app
from pymongo.errors import DuplicateKeyError
import os

@celery.task(bind=True)
def insert_documents(self, filename):
  app = create_app()
  records, totalRecords = file_to_records(filename, app.config)
  ignoredRecords = 0
  processedRecords = 0
  jobs_added = 0
  for record in records:
    processedRecords += 1
    try:
      insert_record(record)
      jobs_added += 1
    except DuplicateKeyError as e:
      ignoredRecords += 1
    meta = { 'totalRecords': totalRecords, 'processedRecords': processedRecords, 'ignoredRecords': ignoredRecords, 'jobs_added': jobs_added }
    self.update_state(state='Progress', meta=meta)
    time.sleep(10)
  filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  os.remove(filePath)
  return { 'totalRecords': totalRecords, 'processedRecords': processedRecords, 'ignoredRecords': ignoredRecords, 'jobs_added': jobs_added , 'status': 'Upload Completed'}