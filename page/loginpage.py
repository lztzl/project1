#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/1
# @Author  : Mik
from selenium.webdriver.common.by import By
from setting import PROJECT_01_URL
from enum import Enum, unique
from common.basepage import BasePage


class LoginPage(BasePage):
    @unique
    class LoginPageRsrc(Enum):
        URL_LOGIN = f'{PROJECT_01_URL}/login.html'
        LOC_用户名框 = By.XPATH, '//input[@name="accounts"]'
        LOC_密码框 = By.XPATH, '//input[@name="pwd"]'
        LOC_登陆结果 = By.XPATH, '//p[@class="prompt-msg"]'

    def login(self, user, passwd):
        self.get(self.LoginPageRsrc.URL_LOGIN.value)
        self.send_keys(self.LoginPageRsrc.LOC_用户名框, user)
        self.send_keys(self.LoginPageRsrc.LOC_密码框, passwd)
        self.submit(self.LoginPageRsrc.LOC_用户名框)
        return self.get_text(self.LoginPageRsrc.LOC_登陆结果)
