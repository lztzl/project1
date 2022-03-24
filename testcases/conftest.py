#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/23
# @Author : Mik

import pytest
from setting import DATA_ROOT_PATH
from pom.login import Login
from utils.reader import YamlReader


@pytest.fixture()
def common_login(driver):
    """调用driver对象登录后返回driver对象"""
    data_path = DATA_ROOT_PATH + 'login_data.yaml'
    user_info = YamlReader(data_path).data[0]
    Login(driver).login(user_info[0], user_info[1])
    return driver
