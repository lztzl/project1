#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22
# @Author  : Mik
from selenium.webdriver.common.by import By
from setting import PROJECT_01_URL
from common.basepage import BasePage
from enum import Enum, unique


class UserAddressPage(BasePage):
    @unique
    class UserAddressPageRsrc(Enum):
        URL_Address = f"{PROJECT_01_URL}/useraddress/index.html"
        LOC_新增地址按钮 = By.XPATH, '//*[@data-popup-title="新增地址"]'
        LOC_iframe = By.XPATH, '//iframe[@src="https://maitenghuicai.com/useraddress/saveinfo.html"]'
        LOC_别名框 = By.XPATH, '//input[@placeholder="别名"]'
        LOC_姓名框 = By.XPATH, '//input[@placeholder="姓名"]'
        LOC_电话框 = By.XPATH, '//input[@placeholder="电话"]'
        LOC_详细地址框 = By.XPATH, '//input[@placeholder="详细地址"]'
        LOC_保存按钮 = By.XPATH, '//*[text()="保存"]'
        LOC_省下拉按钮 = By.XPATH, '//span[text()="省份"]'
        LOC_选择省 = By.XPATH, '//li[text()="湖北省"]'
        LOC_市下拉框按钮 = By.XPATH, '//span[text()="城市"]'
        LOC_选择市 = By.XPATH, '//li[text()="武汉市"]'
        LOC_区下拉框按钮 = By.XPATH, '//span[text()="区/县"]'
        LOC_选择区 = By.XPATH, '//li[text()="江夏区"]'
        LOC_添加地址结果 = By.XPATH, '//p[@class="prompt-msg"]'

    def add_address(self, alias, name, phone, address):
        self.find_element_and_send_keys(self.UserAddressPageRsrc.LOC_别名框, alias)
        self.find_element_and_send_keys(self.UserAddressPageRsrc.LOC_姓名框, name)
        self.find_element_and_send_keys(self.UserAddressPageRsrc.LOC_电话框, phone)
        self.find_element_and_send_keys(self.UserAddressPageRsrc.LOC_详细地址框, address)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_省下拉按钮)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_选择省)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_市下拉框按钮)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_选择市)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_区下拉框按钮)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_选择区)
        self.scroll_into_view_by_js(self.UserAddressPageRsrc.LOC_保存按钮)
        self.sleep(1)
        self.find_element_and_click(self.UserAddressPageRsrc.LOC_保存按钮)
        self.sleep(0.5)
        return self.get_text(self.UserAddressPageRsrc.LOC_添加地址结果)
