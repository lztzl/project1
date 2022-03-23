#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik

from page.loginpage import LoginPage
from setting import DATA_ROOT_PATH
from utils.reader import YamlReader
from page.search import SearchResources, SearchCommodity


class AddCommodity:
    user_info = YamlReader(DATA_ROOT_PATH + 'login_data.yaml').data[0]

    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.addcomm = SearchCommodity(driver)

    def add_comm(self):
        self.login.login(self.user_info[0], self.user_info[1])
        self.addcomm.get(SearchResources.URL_search.value)
        self.addcomm.search()

