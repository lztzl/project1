#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11
# @Author  : Mik
from utils.reader import INIReader
from setting import DATABASE_INI_PATH
from aiomysql import create_pool, DictCursor
from cx_Oracle import SessionPool
from asyncio import get_event_loop, ensure_future
from typing import List


class DataBase:

    def __init__(self, database: str = 'mysql', autocommit: bool = True, *args, **kwargs):
        """

        :param database: 数据库类型
        :param autocommit: 是否自动提交事务
        :param args:
        :param kwargs:
        """
        self._args, self._kwargs = args, kwargs
        self._autocommit = autocommit
        if database.lower() == 'mysql':
            self._database = create_pool
            self._ini = INIReader(DATABASE_INI_PATH, section='MYSQL').data
            self._loop = get_event_loop()
            self._mysql_pool = self.mysql_pool
        if database.lower() == 'oracle':
            self._database = SessionPool
            self._ini = INIReader(DATABASE_INI_PATH, section='ORACLE').data
            self._oracle_pool = self.oracle_pool

    @property
    def oracle_pool(self):
        return self._database(*self._args, **self._ini, **self._kwargs)

    @property
    def mysql_pool(self):
        self._ini['autocommit'] = self._autocommit
        pool_task = ensure_future(self._database(*self._args, **self._ini, **self._kwargs))
        self._loop.run_until_complete(pool_task)
        return pool_task.result()


class MysqlClient(DataBase):

    @classmethod
    def setup(cls, *args, **kwargs):
        return cls(
            *args, **kwargs
        )

    async def _select(self, sql: str, param: tuple = (), rows: [int, None] = 1):
        async with self._mysql_pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), param)
                if rows:
                    rs = await cur.fetchmany(rows)
                else:
                    rs = await cur.fetchall()
        return rs

    def select(self, *args, **kwargs):
        #self._loop.run_until_complete(select_task := ensure_future(self._select(*args, **kwargs)))
        return select_task.result()

    async def _execute(self, sql: str, param: tuple = ()):
        async with self._mysql_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql.replace('?', '%s'), param)
                return cur.rowcount

    def execute(self, *args, **kwargs):
        #self._loop.run_until_complete(execute_task := ensure_future(self._execute(*args, **kwargs)))
        return execute_task.result()


class OracleClient(DataBase):

    @classmethod
    def setup(cls, *args, **kwargs):
        return cls(
            'oracle', *args, **kwargs
        )

    def select(self, sql: str, param: [list, None] = None, rows: [int, None] = 1, **kwargs):
        if param and kwargs:
            raise Exception(f'两种参数类型不能同时传入：{param}, {kwargs}')
        with self._oracle_pool.acquire() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (param or kwargs))
                columns = [col[0] for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                if rows:
                    if rows == 1:
                        rs = cur.fetchone()
                    else:
                        rs = cur.fetchmany(rows)
                else:
                    rs = cur.fetchall()
        return rs

    def execute(self, sql: str, param: List[tuple], **kwargs):
        with self._oracle_pool.acquire() as conn:
            with conn.cursor() as cur:
                if param:
                    cur.executemany(sql, param)
                else:
                    cur.execute(sql, **kwargs)
                rowcount = cur.rowcount
            conn.commit()
        return rowcount


# mysql = MysqlClient.setup()
# print(mysql.select(r'SHOW DATABASES', (), rows=None))
# print(mysql.select(r'SELECT * FROM ZT_BUG WHERE ID = ?', (1, )))
# print(mysql.execute(r'UPDATE ZT_BUG SET TITLE = ? WHERE ID = ?', ('演示bug1', 1)))

oracle = OracleClient.setup()
oracle.select(r'SELECT * FROM TABLEA WHERE ID = :ID AND NAME = :SAM', [1, 'SAM'], 1)
oracle.select(r'SELECT * FROM TABLEA WHERE ID = :ID AND NAME = :SAM', rows=1, ID=1, SAM='SAM')
oracle.execute(r'UPDATE DEMO_TABLE SET NAME = :SAM WHERE ID = :ID',
               [('SAM', 1), ('TOM', 2)])
oracle.execute(r'UPDATE DEMO_TABLE SET NAME = :SAM WHERE ID = :ID', param=[], SAM='SAM', ID=1)
