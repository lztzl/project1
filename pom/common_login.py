#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/23
# @Author : Mik

from pom.login import Login
from setting import DATA_ROOT_PATH
from utils.logs import logger
from utils.reader import YamlReader


def common_login(driver):
    data_path = DATA_ROOT_PATH + 'login_data.yaml'
    user_info = YamlReader(data_path).data[0]
    res = Login(driver).login(user_info[0], user_info[1])

    logger.info(res)


