from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api


from resources.login import UserLoginResource
from resources.logout import LogoutResource,jwt_blacklist
from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource
from resources.register import UserRegisterResource

from flask_jwt_extended import JWTManager

app = Flask(__name__)

# 환경 변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header,jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
api.add_resource( UserRegisterResource,'/user/register')
api.add_resource(UserLoginResource, '/user/login')
api.add_resource(LogoutResource, '/user/logout')

if __name__ == "__main__" :
    app.run()

## export FLASK_APP=app.py
## export FLASK_RUN_PORT=5000


#포스트맨을 사용하는 이유
#웹브라우저에서는 get 메소드만 가능하지만 포스트맨에서는 post,put,delete 메소드가 가능하다