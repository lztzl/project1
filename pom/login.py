#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/23
# @Author : Mik
# @File : login.py
import time

from selenium.webdriver.common.by import By
from setting import URL_01
from enum import Enum, unique
from common.basepage import BasePage


@unique
class LoginResources(Enum):
    URL_LOGIN = f'{URL_01}/login.html'
    LOC_用户名框 = By.XPATH, '//input[@name="accounts"]'
    LOC_密码框 = By.XPATH, '//input[@name="pwd"]'
    LOC_登陆结果 = By.XPATH, '//p[@class="prompt-msg"]'


class Login(BasePage):

    def login(self, user, passwd):
        self.get(LoginResources.URL_LOGIN.value)
        self.send_keys(LoginResources.LOC_用户名框, user)
        self.send_keys(LoginResources.LOC_密码框, passwd)
        self.submit(LoginResources.LOC_用户名框)
        self.sleep(0.5)
        return self.get_text(LoginResources.LOC_登陆结果)