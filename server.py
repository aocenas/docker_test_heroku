# https://github.com/kennethreitz/flask-heroku

from typing import Dict
import traceback
from datetime import datetime, timedelta
import os

from flask import Flask
from flask import jsonify

# import numpy as np

app = Flask(__name__)


@app.route('/test')
def score():
    return jsonify({'message': 'hello'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
