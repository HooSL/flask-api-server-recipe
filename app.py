from flask import Flask,request
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api

app = Flask(__name__)



if __name__ == "__main__":
    app.run()

## export FLASK_APP = app.py
## export FLASK_RUN_PORT = 5000