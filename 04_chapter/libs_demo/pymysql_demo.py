# pymysql_demo.py
import pymysql.cursors

# 连接数据库
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='dev4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection as conn:
    with conn.cursor() as cursor:
        # 查询auth_user表
        sql = "SELECT `id`, `name`, `email` FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

