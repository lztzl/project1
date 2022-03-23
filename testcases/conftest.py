#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/23
# @Author : Mik

# import pytest
# from setting import  DATA_ROOT_PATH
# from utils.logs import logger
# from pom.login import Login
# from utils.reader import YamlReader

#
# @pytest.fixture()
# def common_login(driver):
#     data_path = DATA_ROOT_PATH + 'login_data.yaml'
#     user_info = YamlReader(data_path).data
#     res = Login(driver).login(user_info[0], user_info[1])
#     logger.info(res)
