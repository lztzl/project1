#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from setting import PROJECT_01_URL
from enum import Enum, unique


@unique
class HomePageResources(Enum):
    URL_HOME = PROJECT_01_URL
    LOC_登录按钮 = By.XPATH, '//*[text()="登录"]'
    LOC_注册按钮 = By.XPATH, '//*[text()="注册"]'
    LOC_搜索框 = By.ID, "search-input"
    LOC_搜索按钮 = By.XPATH, '//span[text()="搜索"]'
    LOC_个人中心 = By.XPATH, '//*[text()="个人中心"]'


class HomePage(BasePage):
    pass
