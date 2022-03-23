#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik


from selenium.webdriver.common.by import By
from common.basepage import BasePage
from setting import PROJECT_01_URL
from enum import Enum, unique


@unique
class SearchResources(Enum):
    URL_search = PROJECT_01_URL
    LOC_搜索框 = By.ID, "search-input"
    LOC_搜索按钮 = By.ID, "ai-topsearch"
    LOC_物品品框 = By.XPATH, '//ul[@class="am-avg-sm-2 am-avg-md-3 am-avg-lg-5 am-margin-top-sm search-list"]/li[1]'
    LOC_商品型号 = By.XPATH, '//*[@class="theme-options sku-items"]/ul/li[1]'
    LOC_加入购物车 = By.XPATH, '//*[@title="加入购物车"]'


class SearchCommodity(BasePage):

    def search(self):
        self.send_keys(SearchResources.LOC_搜索框, '鞋')
        self.click(SearchResources.LOC_搜索按钮)
        hand = self.get_handles()
        self.click(SearchResources.LOC_物品品框)
        self.switch_window(hand)
        self.click(SearchResources.LOC_商品型号)
        self.click(SearchResources.LOC_加入购物车)

