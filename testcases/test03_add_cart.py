#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/24
# @Author : Mik

import allure

from utils.logs import logs
from pom.add_cart_from_home import AddCart
import time


@allure.epic('Web测试')
@allure.severity('blocker')
@allure.feature('购物流程')
class TestAddCart:
    def setup(self):
        pass

    def teardown(self):
        time.sleep(3)

    @allure.story('正常购物')
    @allure.title('测试数据')
    @logs
    def test01(self, common_login):
        page = AddCart(common_login)
        res = page.add_cart()
        assert res == "加入成功"
