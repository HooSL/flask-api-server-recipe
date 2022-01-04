from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

from email_validator import validate_email, EmailNotValidError

class UserRegisterResource (Resource):
    def post(self):

        #1. 클라이언트가 보내준, 회원 정보를 받아온다.
        data = request.get_json()
        #data에는 {"username":"아무개","email":"qqq@gmail.com","password":"abc123@"} 들어있다

        #2. 이메일 주소가 제대로 된 주소인지 확인하는 코드 잘못된 이메일이면 잘못됐다고 응답한다


        #3. 비밀번호 길이같은 소전이 있는지 확인하는 코드 잘못됐으면, 클라이언트에 응답한다.

        #4. 비밀번호를 암호화한다.

        #5. 데이터를 DB에 저장한다.

        #6. username이나 email이 이미 DB에 있으면, 이미 존재하는 회원이라고 클라이언트에 응답한다.

        #7. 모든것이 정상이면, 회원가입 잘 되었다고 응답한다.

        return







