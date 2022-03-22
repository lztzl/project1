#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik

from page.loginpage import LoginPage
from page.user_address_page import UserAddressPage,UserAddressPageRsrc
from setting import DATA_ROOT_PATH
from utils.reader import YamlReader


class ChangeUserAddress:
    user_info = YamlReader(DATA_ROOT_PATH + 'login_data.yaml').data[0]

    def __init__(self, driver):
        self.login_page_obj = LoginPage(driver)
        self.user_address_page_obj = UserAddressPage(driver)

    def add_address_form_homopage(self, alias, name, phone, address):
        self.login_page_obj.login(self.user_info[0], self.user_info[1])
        self.user_address_page_obj.get(UserAddressPageRsrc.URL_Address.value)
        self.user_address_page_obj.click(UserAddressPageRsrc.LOC_新增地址按钮)
        self.user_address_page_obj.switch_iframe(UserAddressPageRsrc.LOC_iframe)
        res = self.user_address_page_obj.add_address(alias, name, phone, address)
        self.user_address_page_obj.screenshot(
            UserAddressPageRsrc.LOC_添加地址结果)
        return res
