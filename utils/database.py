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
        self.db.ping()
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
        self.db.ping()
        cur = self.db.cursor()  # 获取游标
        sql = sql.lower()
        try:
            cur.execute(sql)
        except Exception:
            self.db.rollback()
            cur.close()
            raise
        cur.close()

# sql1 = "select * from Student RIGHT JOIN (select t1.SId, class1, class2 from (select SId, score as class1 from sc where sc.CId = '01') as t1, (select SId, score as class2 from sc where sc.CId = '02')as t2 where t1.SId = t2.SId AND t1.class1 > t2.class2) as r on Student.SId = r.SId;"
#
#
# mysql = MysqlClient()
# data = mysql.select(sql1)
# print(data)
