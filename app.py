from flask import Flask, request
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api
from resources.login import UserLoginResource

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResouce
from resources.register import UserRegisterResource

app = Flask(__name__)

#JWP 토큰 만들기
jwp = JWPManager()

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResouce,'/recipes/<int:recipe_id>/publish')
api.add_resource(UserRegisterResource,'/user/register')
api.add_resource(UserLoginResource,'/user/login')

if __name__ == "__main__" :
    app.run()

## export FLASK_APP=app.py
## export FLASK_RUN_PORT=5000


#포스트맨을 사용하는 이유
#웹브라우저에서는 get 메소드만 가능하지만 포스트맨에서는 post,put,delete 메소드가 가능하다