from flask import g
from helpers.db_helper import connect_db
from routes.file_upload_routes import file_upload
from app import create_app

app = create_app()

# setting mongo client and redis client on request context using two connector functions
@app.before_request
def before_request():
    g.db = connect_db(app)

# closing db on request teardown
@app.teardown_request
def teardown_request(exception):
    if hasattr(g,'db'):
        g.db.close()

# register blueprint for file_upload and task_runner endpoints
app.register_blueprint(file_upload)

# bootstraping the app
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    