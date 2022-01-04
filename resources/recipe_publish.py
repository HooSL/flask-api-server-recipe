from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

class RecipePublishResouce(Resource):
    def put(self,recipe_id):
        try:
            #1. DB에 연결
            connection = get_connection()
            
            query = '''update recipe
                        set is_publish = 1
                        where id = %s;'''
            #2-1. 파이썬에서 튜플을 만들때 데이터가 1개인 경우에는 ,를 꼭 작성해준다.
            record = (recipe_id,)

            #3. 커넥션으로부터 커서를 가져온다
            cursor = connection.cursor()

            #4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query,record)

            #5. 커넥션을 커밋한다 -> 디비에 영구적으로 반영하라는 뜻
            connection.commit()

        except Error as e:
            print('Error',e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

        return {'result':'레시피가 공개로 설정되었습니다.'},HTTPStatus.OK

    def delete(self,recipe_id):
        #delete에선 body담지 않기
        try:
            #1. DB에 연결
            connection = get_connection()
            
            query = '''update recipe
                        set is_publish = 0
                        where id = %s;'''
            #2-1. 파이썬에서 튜플을 만들때 데이터가 1개인 경우에는 ,를 꼭 작성해준다.
            record = (recipe_id,)

            #3. 커넥션으로부터 커서를 가져온다
            cursor = connection.cursor()

            #4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query,record)

            #5. 커넥션을 커밋한다 -> 디비에 영구적으로 반영하라는 뜻
            connection.commit()

        except Error as e:
            print('Error',e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

        return {'result':'레시피가 임시저장 되었습니다.'},HTTPStatus.OK
