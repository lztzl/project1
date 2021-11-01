#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 
# @Author  : Mik
from os.path import exists
from utils.logs import logger
from yaml import safe_load_all, safe_load
from configparser import ConfigParser


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class File:

    def __init__(self, file_path: str):
        """检查文件是否存在"""
        if not exists(file_path):
            logger.info("加载文件不存在，请检查。")
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):
    def __init__(self, yml_path: str, multi: bool = False):
        """
        :param yml_path: 文件路径
        :param multi: 是否多段
        """
        super(YamlReader, self).__init__(yml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:  # 判断文件是否已经打开
            logger.info(f"加载文件:{self._file_path}")
            with open(self._file_path, 'rb') as fp:
                if self._multi:  # 判断文件是否多节，如果多节转化为列表返回
                    self._data = list(safe_load_all(fp))
                else:
                    self._data = safe_load(fp)
        return self._data


class INIReader(File):

    def __init__(self, ini_path: str, section: str):
        super(INIReader, self).__init__(ini_path)
        self._data = {}
        self._section = section
        self._parser = MyConfigParser()

    @property
    def data(self):
        """
        :return: dict
        """
        if not self._data:
            logger.info(f'加载文件：{self._file_path}')
            self._parser.read(self._file_path, encoding='UTF-8')
            for k, v in self._parser.items(self._section):
                # 将数据转换成int
                self._data[k] = int(v) if k in ('port', 'maxsize', 'minsize', 'max', 'min', 'increment') else v
        return self._data


# da = INIReader(r'E:\My_code\UIAutoTest\config\appcfg.ini', section='desired').data
# print(da, type(da))

# from setting import DATA_ROOT_PATH
#
# data = YamlReader(DATA_ROOT_PATH + 'user_address_info_data.yaml').data
# # data = data.get('login_pass')
# print(data,type(data))