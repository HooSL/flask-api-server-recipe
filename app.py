from flask import Flask, request
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource

app = Flask(__name__)

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>')


if __name__ == "__main__" :
    app.run()

## export FLASK_APP=app.py
## export FLASK_RUN_PORT=5000