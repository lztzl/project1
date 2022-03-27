#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/27
# @Author : Mik
import pymysql
from utils.reader import INIReader
from setting import DATABASE_INI_PATH
from typing import List


class MysqlClient:
    def __init__(self, autocommit=True, **kwargs):
        db_config = INIReader(DATABASE_INI_PATH, 'MYSQL').data
        self.db = pymysql.connect(autocommit=autocommit, **db_config, **kwargs)  # 建立连接

    def __del__(self):
        self.db.close()  # 关闭连接

    def select(self, sql):
        """
        查询
        :param sql:
        :return:
        """
        cur = self.db.cursor()  # 获取游标
        sql = sql.lower()
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def execute_sql(self, sql):
        """
        执行sql
        :param sql:
        :return:
        """

        cur = self.db.cursor()  # 获取游标
        sql = sql.lower()
        try:
            cur.execute(sql)
        except Exception:
            self.db.rollback()
            cur.close()
            raise
        cur.close()


# sql1 = "SELECT * FROM course;"
#
# mysql = MysqlClient()
# data = mysql.select(sql1)
# print(data)
# sql2 = "insert into Student values('08' , '孙唯一' , '2014-06-01' , '男');"
# mysql.execute_sql(sql2)

