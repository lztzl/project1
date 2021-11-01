#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11
# @Author  : Mik

import logging
from functools import wraps
import datetime
from setting import LOG_PATH


def creation_logger(level):
    """
    日志器
    :param level: 设置日志级别
    :return:
    """
    # 设置路径
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
    path_file = f'{LOG_PATH}{now_time}.log'
    # 创建日志器
    log = logging.getLogger()
    log.setLevel(level=level)
    # 创建格式器
    file_formatter = logging.Formatter(
        fmt='[%(asctime)s] [%(levelname)s] [%(filename)s line:%(lineno)d]->>%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    # 创建文件输出器
    f_hand = logging.FileHandler(filename=path_file, encoding='utf-8')
    f_hand.setFormatter(file_formatter)
    log.addHandler(f_hand)
    return log


Level = logging.INFO
logger = creation_logger(Level)


def logs(func):
    """
    兼容日志装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrap_func(*args, **kwargs):
        tuple_args = args
        dict_kwargs = kwargs
        try:
            func(*args, **kwargs)
            logger.debug(
                f'{func.__name__}(*args: tuple = {tuple_args}, **kwargs: dict = {dict_kwargs})',
                extra={'status': 'PASS'}
            )
        except Exception:
            logger.exception(
                f'{func.__name__}(*args: tuple = {tuple_args}, **kwargs: dict = {dict_kwargs})',
                exc_info=True,
                extra={'status': 'FAIL'}
            )
            raise

    return wrap_func


# @logs
# def test(a, b):
#     logger.info('正在测试')
#     assert b == a
#
#
# test(a=2, b=2)
