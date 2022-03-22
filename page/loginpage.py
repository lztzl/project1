#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/1
# @Author  : Mik
from selenium.webdriver.common.by import By
from setting import PROJECT_01_URL
from enum import Enum, unique
from common.basepage import BasePage


@unique
class LoginPageRsrc(Enum):
    URL_LOGIN = f'{PROJECT_01_URL}/login.html'
    LOC_用户名框 = By.XPATH, '//input[@name="accounts"]'
    LOC_密码框 = By.XPATH, '//input[@name="pwd"]'
    LOC_登陆结果 = By.XPATH, '//p[@class="prompt-msg"]'


class LoginPage(BasePage):

    def login(self, user, passwd):
        self.get(LoginPageRsrc.URL_LOGIN.value)
        self.send_keys(LoginPageRsrc.LOC_用户名框, user)
        self.send_keys(LoginPageRsrc.LOC_密码框, passwd)
        self.submit(LoginPageRsrc.LOC_用户名框)
        return self.get_text(LoginPageRsrc.LOC_登陆结果)
