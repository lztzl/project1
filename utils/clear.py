#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 
# @Author  : Mik

import os
import time
from utils.logs import logger


def clear_img(dir_path):
    """
    清除截图
    :param dir_path: 目录路径
    :return: None
    """

    if os.path.exists(dir_path) and os.path.isdir(dir_path):  # 确认路径是否存在
        logger.info('开始清理截图')
        ls = os.listdir(dir_path)
        for i in ls:
            c_path = os.path.join(dir_path, i)  # 将目录和文件名拼接
            if os.path.isdir(c_path):  # 如果是目录继续调用清除函数
                clear_img(c_path)
            else:
                if ".gitkeep" in c_path:
                    pass
                else:
                    os.remove(c_path)
        logger.info('清除截图完成')
    else:
        logger.info('没有找到目录，请检查路径是否存在')
        raise NameError('路径不存在或者不是一个目录')


def clear_log(dir_path):
    """
    清空一天前生成的log
    :param dir_path: 目录路径
    :return: None
    """

    now_time = time.time()  # 获取现在时间戳
    if os.path.exists(dir_path) and os.path.isdir(dir_path):  # 判断路径是目录并且路径下有文件或者目录
        logger.info('开始清理log')
        ls = os.listdir(dir_path)
        for i in ls:
            c_path = os.path.join(dir_path, i)  # 将目录和文件名拼接
            if os.path.isdir(c_path):
                clear_log(c_path)
            else:
                cre_time = os.path.getmtime(c_path)  # 获取文件创建时间戳
                if cre_time < (now_time - 86400) and (".gitkeep" not in c_path):  # 删除符合条件文件
                    os.remove(c_path)
        logger.info('log清理完成')
    else:
        logger.info('没有找到路径，请确认路径是否存在')
        raise NameError('路径不存在或者不是一个目录')

# clearLog(root_dir+r'\log')
