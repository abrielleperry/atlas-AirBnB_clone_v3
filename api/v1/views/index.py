#!/bin/usr/python3
""" retruns json response status of API """
from flask import Flask, jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ checks status of API """
    return jsonify({"status":"OK"})

@app_views.route('/api/v1/stats')
def close_db():
    """ closes db """
    return storage.close()



if __name__ == '__main__':
    app_views.run(debug=True, host='0.0.0.0', port='5000')
