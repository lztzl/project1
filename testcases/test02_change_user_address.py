#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik

import allure

from setting import DATA_ROOT_PATH
from utils.reader import YamlReader
from utils.logs import logs
from pom.change_user_address import ChangeUserAddress
import time


@allure.epic('Web测试')
@allure.severity('blocker')
@allure.feature('修改地址模块')
class TestAddress:
    def setup(self):
        self.address_info = YamlReader(DATA_ROOT_PATH + 'user_address_info_data.yaml').data[0]

    def teardown(self):
        time.sleep(3)

    @allure.story('正常修改地址')
    @allure.title('测试数据')
    @logs
    def test01_add_address(self, driver):
        page = ChangeUserAddress(driver)
        res = page.add_address_form_homopage(self.address_info[0], self.address_info[1], self.address_info[2],
                                             self.address_info[3])
        assert res == self.address_info[4]['expect']
