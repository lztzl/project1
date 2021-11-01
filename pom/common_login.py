#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 
# @Author  : Mik

from page.loginpage import LoginPage


class CommonLogin:
    def __init__(self, driver):
        self.login_page_obj = LoginPage(driver)

    def login_result(self, user, passwd):
        return self.login_page_obj.login(user, passwd)
