#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 
# @Author  : Mik

import allure
import pytest
from utils.logs import logs
from pom.common_login import CommonLogin
from setting import DATA_ROOT_PATH
from utils.reader import YamlReader
import time


@allure.epic('Web测试')
@allure.severity('blocker')
@allure.feature('用户登录模块')
class TestLogin:
    data_path = DATA_ROOT_PATH + 'login_data.yaml'
    user_info = YamlReader(data_path).data

    def setup(self):
        pass

    def teardown(self):
        time.sleep(3)

    @allure.story('用户登陆')
    @allure.title('测试数据')
    @pytest.mark.parametrize("arg", user_info)
    @logs
    def test01_login(self, driver, arg):
        page = CommonLogin(driver)
        res = page.login_result(arg[0], arg[1])
        assert res == arg[2]
