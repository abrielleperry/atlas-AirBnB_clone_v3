#!/bin/usr/python3
""" initializes Flask application """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)



@app.teardown_appcontext
def close_db():
    """ closes db """
    return storage.close()

@app.errorhandler(404)
def not_found(error):
    response = jsonify({'status': 404,'error': 'not found'})
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)
