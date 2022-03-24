#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/23
# @Author : Mik

from selenium.webdriver.common.by import By
from common.basepage import BasePage
from setting import URL_01
from enum import Enum, unique


@unique
class AddCartResources(Enum):
    URL_search = URL_01
    LOC_搜索框 = By.ID, "search-input"
    LOC_搜索按钮 = By.ID, "ai-topsearch"
    LOC_物品品框 = By.XPATH, '//ul[@class="am-avg-sm-2 am-avg-md-3 am-avg-lg-5 am-margin-top-sm search-list"]/li[1]'
    LOC_商品型号 = By.XPATH, '//*[@class="theme-options sku-items"]/ul/li[1]'
    LOC_加入购物车 = By.XPATH, '//*[@title="加入购物车"]'
    LOC_添加结果 = By.XPATH, '//*[@class="prompt-content"]'


class AddCart(BasePage):

    def add_cart(self):
        self.send_keys(AddCartResources.LOC_搜索框, '鞋')
        self.click(AddCartResources.LOC_搜索按钮)
        hand = self.get_handles()
        self.click(AddCartResources.LOC_物品品框)
        self.switch_window(hand)
        self.click(AddCartResources.LOC_商品型号)
        self.sleep(1)
        self.click(AddCartResources.LOC_加入购物车)
        res = self.get_text(AddCartResources.LOC_添加结果)
        return res
