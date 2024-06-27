from typing import Any

import pymysql.cursors


class SQLBase:
    """SQL base API"""

    @staticmethod
    def dict_to_str(data: dict) -> str:
        """
        字典转字符串，用逗号分割
        """
        tmp_list = []
        for key, value in data.items():
            if value is None:
                tmp = f"{key}=null"
            elif isinstance(value, int):
                tmp = f"{key}={value}"
            else:
                tmp = f"{key}='{value}'"
            tmp_list.append(tmp)
        return ','.join(tmp_list)

    @staticmethod
    def dict_to_str_and(conditions: dict) -> str:
        """
        字典转字符串 用 and 连接
        """
        tmp_list = []
        for key, value in conditions.items():
            if value is None:
                tmp = f"{key}=null"
            elif isinstance(value, int):
                tmp = f"{key}={value}"
            else:
                tmp = f"{key}='{value}'"
            tmp_list.append(tmp)
        return ' and '.join(tmp_list)


class MySQLDB(SQLBase):
    """MySQL DB API"""

    def __init__(self,
                 host: str,
                 port: int,
                 user: str,
                 password: str,
                 database: str,
                 charset: str = "utf8mb4") -> None:
        """
        连接 MySQL DB
        :param host: 地址
        :param port: 端口
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名
        :param charset: 编码类型
        """
        self.connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor)

    def execute_sql(self, sql: str) -> None:
        """
        执行 SQL 语句
        """
        with self.connection.cursor() as cursor:
            self.connection.ping(reconnect=True)
            if "delete" in sql.lower()[0:6]:
                cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sql)
        self.connection.commit()

    def query_sql(self, sql: str) -> list:
        """
        查询 SQL 语句
        """
        data_list = []
        with self.connection.cursor() as cursor:
            self.connection.ping(reconnect=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                data_list.append(row)
            self.connection.commit()
            return data_list

    def query_one(self, sql: str) -> Any:
        """
        查询 SQL 语句，返回一条数据
        """
        with self.connection.cursor() as cursor:
            self.connection.ping(reconnect=True)
            cursor.execute(sql)
            row = cursor.fetchone()
            self.connection.commit()
            return row

    def insert(self, table: str, data: dict) -> None:
        """
        插入数据
        :param table: 表名
        :param data: 数据
        """
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        sql = f"""insert into {table} ({key}) values ({value})"""
        self.execute_sql(sql)

    def select(self, table: str, where: dict = None, one: bool = False) -> Any:
        """
        查询数据
        :param table: 表名
        :param where: 条件
        :param one: 是否返回一条数据
        """
        sql = f"""select * from {table} """
        if where is not None:
            sql += f""" where {self.dict_to_str_and(where)}"""
        if one is True:
            return self.query_one(sql)

        return self.query_sql(sql)

    def update(self, table: str, data: dict, where: dict) -> None:
        """
        更新数据
        :param table: 表名
        :param data: 更新字段
        :param where: 查询条件
        """
        sql = f"""update {table} set """
        sql += self.dict_to_str(data)
        if where:
            sql += f""" where {self.dict_to_str_and(where)};"""
        self.execute_sql(sql)

    def delete(self, table: str, where: dict = None) -> None:
        """
        删除数据
        :param table: 表名
        :param where: 查询条件
        """
        sql = f"""delete from {table}"""
        if where is not None:
            sql += f""" where {self.dict_to_str_and(where)};"""
        self.execute_sql(sql)
