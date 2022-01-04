from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

from flask_jwt_extended import jwt_required, get_jwt_identity

# 클래스 작성 : 변수와 함수로 구성된 묶음 
# 클래스는 상속이 가능하다!
# 아래 클래스는, flask_restful 라이브러리의
# Resource 클래스를 상속한 것이다.
class RecipeListResource(Resource) :
    def get(self):
        # 클라이언트가 GET 요청하면, 이 함수에서
        # 우리가 코드를 작성해 주면 된다.

        # 1. db 접속recipe 테이블에서 select 
        try :
            connection = get_connection()

            query = ''' select * 
                        from recipe ; '''
            
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            ### 중요. 파이썬의 시간은, JSON으로 보내기 위해서
            ### 문자열로 바꿔준다.
            i = 0
            for record in record_list:
                record_list[i]['created_at'] = record['created_at'].isoformat()
                record_list[i]['updated_at'] = record['updated_at'].isoformat()
                i = i + 1
            
        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            print('Error while connecting to MySQL', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            print('finally')
            cursor.close()
            if connection.is_connected():
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')


        return {'data' :record_list} , HTTPStatus.OK


    @jwt_required()   # 이 함수의 optional 파라미터가 False면, 무조건 토큰이 있어야 호출가능
    def post(self) :

        # 클라이언트의 body로 보낸 json 데이터는
        # request.get_json() 함수로 받는다.
        data = request.get_json()
        #   data = { 'name' : '된장찌게', 'description' : '두부 된장찌게 끓이는법',
        # 'num_of_servings' : 6, 'cook_time' : 35, 
        # 'directions':'두부 넣고 물넣고 된장넣고 끓인다.', 'user_id' : 1}

        print(data)

        user_id = get_jwt_identity()

        try :
            # 1. DB 에 연결
            connection = get_connection()
           
            # 2. 쿼리문 만들고
            query = '''insert into recipe
                    (name, description, num_of_servings, cook_time, directions,
                    user_id)
                    values
                    (%s, %s, %s, %s, %s, %s);'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (data['name'], data['description'], data['num_of_servings'],
                        data['cook_time'], data['directions'], user_id  )
            
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋한다.=> 디비에 영구적으로 반영하라는 뜻.
            connection.commit()

        except Error as e:
            print('Error ', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

        return {'result' : '잘 저장되었습니다.'} , HTTPStatus.OK


