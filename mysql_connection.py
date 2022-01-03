import mysql.connector

def get_connection():
    connection=mysql.connector.connect(host = 'dbfoot.cnsfwt1k1yag.ap-northeast-2.rds.amazonaws.com',database='recipe_db',user='recipe_user',password='2105')
    return connection