#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11
# @Author  : Mik
from typing import Union, Type
from selenium.webdriver import *
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from setting import *
from utils.logs import logger

# 自定义异常参数
BROWSERS = (Chrome, Ie, Firefox, Edge, Opera, Safari)
OPTIONS = (ChromeOptions, IeOptions, FirefoxOptions, EdgeOptions, OperaOptions)


class BrowserTypeError(Exception):
    """
    自定义异常类
    """

    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'Unsupported browser parameters:{self._type}'


class Browser:
    # 浏览器驱动路径
    REMOTE_EXECUTOR = COMMAND_REMOTE_EXECUTOR
    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
    FIREFOX_DRIVER_PATH = FIREFOX_DRIVER_PATH
    EDGE_DRIVER_PATH = EDGE_DRIVER_PATH
    OPERA_DRIVER_PATH = OPERA_DRIVER_PATH
    IE_DRIVER_PATH = IE_DRIVER_PATH
    # 启动grid配置
    GRID_MARK = GRID_MARK

    def __init__(self, browser_type: Type[Union[Chrome, Ie, Firefox, Edge, Opera, Safari]] = Chrome,
                 option_type: Type[
                     Union[FirefoxOptions, ChromeOptions, IeOptions, EdgeOptions, OperaOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        if not issubclass(browser_type, BROWSERS):  # 异常处理
            raise BrowserTypeError(browser_type)  # TypeError
        if not issubclass(option_type, OPTIONS):
            raise BrowserTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError
        self._driver = browser_type
        self._option = option_type
        self._path = driver_path
        self._remote = Remote


class MyChrome(Browser):

    @property
    def _option1(self):
        """
        chrome浏览器特有的操作属性
        :return:
        """
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0  # 禁用下载弹窗
        }

        chrome_experimental = {
            # 'mobileEmulation': {'deviceName': 'iPhone 6'},  # 设置手机模式
            'excludeSwitches': ['enable-automation'],  # 反爬设置
        }

        chrome_option = self._option()  # 获取chrome_option实例
        chrome_option.headless = False
        chrome_option.add_argument('--disable-gpu')  # 禁bug，谷歌推荐参数
        chrome_option.add_argument('--ignore-certificate-errors')  # 禁用ssl证书
        chrome_option.add_experimental_option("prefs", prefs)
        for k, v in chrome_experimental.items():
            chrome_option.add_experimental_option(k, v)
        return chrome_option

    def browser(self, option_id: int):
        """
        启动chrome浏览器进行初始配置
        :return:
        """
        if option_id == 0:
            option = None
        elif option_id == 1:
            option = self._option1
        else:
            raise ValueError('Option id error')

        if self.GRID_MARK:  # 判断是否启动GRID
            chrome = self._remote(command_executor=self.REMOTE_EXECUTOR,
                                  desired_capabilities=DesiredCapabilities.CHROME.copy(),
                                  options=option)
        else:
            chrome = self._driver(executable_path=self._path, options=option)
        chrome.maximize_window()
        return chrome


class IE(Browser):

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH

        )

    @property
    def _option1(self):
        """
        ie浏览器特有的操作属性
        :return:
        """
        ie_option = self._option()
        ie_option.browser_attach_timeout = 10000  # ie页面超时时间
        ie_option.ensure_clean_session = True  # ie浏览器清空本地会话
        return ie_option

    def browser(self, option_id: int):
        """
        启动ie浏览器并进行初始配置
        :return:
        """
        if option_id == 0:
            option = None
        elif option_id == 1:
            option = self._option1
        else:
            raise ValueError('Option id error')

        if self.GRID_MARK:
            ie = self._remote(command_executor=self.REMOTE_EXECUTOR,
                              desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy(),
                              options=option)
        else:
            ie = self._driver(executable_path=self._path, options=option)

        ie.maximize_window()
        return ie


class MyFirefox(Browser):

    def __init__(self):
        super(MyFirefox, self).__init__(
            browser_type=Firefox,
            option_type=FirefoxOptions,
            driver_path=super().FIREFOX_DRIVER_PATH
        )

    @property
    def _option1(self):
        """
        firefox浏览器特有的操作属性
        :return:
        """
        firefox_option = self._option()  # 获取chrome_option实例
        firefox_option.headless = False
        return firefox_option

    def browser(self, option_id: int):
        """
        启动firefox浏览器并进行初始配置
        :return:
        """
        if option_id == 0:
            option = None
        elif option_id == 1:
            option = self._option1
        else:
            raise ValueError('Option id error')

        if self.GRID_MARK:  # 判断是否启动GRID
            firefox = self._remote(command_executor=self.REMOTE_EXECUTOR,
                                   desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
                                   options=option)
        else:
            firefox = self._driver(executable_path=self._path, options=option)

        firefox.maximize_window()
        return firefox


class MyEdge(Browser):

    def __init__(self):
        super(MyEdge, self).__init__(
            browser_type=Edge,
            option_type=EdgeOptions,
            driver_path=super().EDGE_DRIVER_PATH
        )

    @property
    def _option1(self):
        """
        ie浏览器特有的操作属性
        :return:
        """
        edge_option = self._option()
        edge_option.page_load_strategy = 'normal'
        return edge_option

    def browser(self, option_id):
        """
        启动edge浏览器并进行初始配置
        :return:
        """
        if option_id == 0:
            option = None
        elif option_id == 1:
            option = self._option1
        else:
            raise ValueError('Option id error')

        if self.GRID_MARK:
            edge = self._remote(command_executor=self.REMOTE_EXECUTOR,
                                desired_capabilities=DesiredCapabilities.EDGE.copy(),
                                options=option)
        else:
            edge = self._driver(executable_path=self._path, options=option)

        edge.maximize_window()
        return edge


class MySafari(Browser):

    def __init__(self):
        super(MySafari, self).__init__(
            browser_type=Safari,
        )

    @property
    def browser(self):
        """
        启动edge浏览器并进行初始配置
        :return:
        """
        if self.GRID_MARK:
            safari = self._remote(command_executor=self.REMOTE_EXECUTOR,
                                  desired_capabilities=DesiredCapabilities.SAFARI.copy())
        else:
            safari = self._driver()
        safari.maximize_window()
        return safari
