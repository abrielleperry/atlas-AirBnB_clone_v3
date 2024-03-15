#!/bin/usr/python3
""" simple single server """
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)



@app.route('@app.teardown_appcontext')
def close_db():
    """ closes db """
    return storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)
