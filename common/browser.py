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
        return f'不支持的浏览器参数:{self._type}'


class Browser:
    # 浏览器驱动路径
    COMMAND_EXC = COMMAND_EXC
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

    @property
    def browser(self):
        """
        subclass should implement this method
        return the instance of WebDriver
        :return:
        """
        return

    @property
    def _options(self):
        """
        subclass should implement this method
        return instance of the Option Type like ChromeOptions
        :return:
        """
        return


class CHROME(Browser):
    METHOD_MARK = CHROME_METHOD_MARK

    OPTION_MARK = CHROME_OPTION_MARK

    HEADLESS = CHROME_HEADLESS

    EXPERIMENTAL = CHROME_EXPERIMENTAL

    PREFS = CHROME_PREFS

    @property
    def _options(self):
        """
        chrome浏览器特有的操作属性
        :return:
        """
        chrome_option = self._option()  # 获取chrome_option实例
        chrome_option.headless = self.HEADLESS
        chrome_option.add_argument('--disable-gpu')  # 禁bug，谷歌推荐参数
        chrome_option.add_argument('--ignore-certificate-errors')  # 禁用ssl证书
        chrome_option.add_experimental_option("prefs", self.PREFS)
        if self.EXPERIMENTAL:
            for k, v in self.EXPERIMENTAL.items():
                chrome_option.add_experimental_option(k, v)
        return chrome_option

    @property
    def browser(self):
        """
        启动chrome浏览器进行初始配置
        :return:
        """
        logger.info('打开chrome浏览器')
        if self.GRID_MARK:  # 判断是否启动GRID

            if self.OPTION_MARK:  # 判断是否执行启动参数
                chrome = self._remote(command_executor=self.COMMAND_EXC,
                                      desired_capabilities=DesiredCapabilities.CHROME.copy(),
                                      options=self._options)  # 得到远程chrome浏览器实例
            else:
                chrome = self._remote(command_executor=self.COMMAND_EXC,
                                      desired_capabilities=DesiredCapabilities.CHROME.copy())
        else:
            if self.OPTION_MARK:
                chrome = self._driver(executable_path=self._path, options=self._options)  # 得到chrome浏览器实例
            else:
                chrome = self._driver(executable_path=self._path)

        if self.METHOD_MARK:  # 判断是否配置浏览器启动操作
            # chrome.implicitly_wait(self.IMPLICITLY_WAIT_TIME)
            # chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
            # chrome.set_script_timeout(self.SCRIPT_TIMEOUT)
            chrome.maximize_window()
            return chrome
        return chrome


class IE(Browser):
    OPTION_MARK = IE_OPTION_MARK

    METHOD_MARK = IE_METHOD_MARK

    CLEAN_SESSION = IE_CLEAN_SESSION

    ATTACH_TIMEOUT = IE_ATTACH_TIMEOUT

    WINDOW_SIZE = IE_WINDOW_SIZE

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH

        )

    @property
    def _options(self):
        """
        ie浏览器特有的操作属性
        :return:
        """
        ie_option = self._option()
        ie_option.browser_attach_timeout = self.ATTACH_TIMEOUT
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        """
        启动ie浏览器并进行初始配置
        :return:
        """
        if self.GRID_MARK:
            if self.OPTION_MARK:
                ie = self._remote(command_executor=self.COMMAND_EXC,
                                  desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy(),
                                  options=self._options)
            else:
                ie = self._remote(command_executor=self.COMMAND_EXC,
                                  desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        else:
            if self.OPTION_MARK:
                ie = self._driver(executable_path=self._path, options=self._options)
            else:
                ie = self._driver(executable_path=self._path)
        if IE_METHOD_MARK:
            # ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
            # ie.set_script_timeout(self.SCRIPT_TIMEOUT)
            ie.maximize_window()
            if self.WINDOW_SIZE:
                ie.set_window_size(*self.WINDOW_SIZE)
        return ie


class FIREFOX(Browser):
    OPTION_MARK = FIREFOX_OPTION_MARK

    METHOD_MARK = FIREFOX_METHOD_MARK

    WINDOW_SIZE = FIREFOX_WINDOW_SIZE

    HEADLESS = FIREFOX_HEADLESS

    def __init__(self):
        super(FIREFOX, self).__init__(
            browser_type=Firefox,
            option_type=FirefoxOptions,
            driver_path=super().FIREFOX_DRIVER_PATH
        )

    @property
    def _options(self):
        """
        firefox浏览器特有的操作属性
        :return:
        """
        firefox_option = self._option()  # 获取chrome_option实例
        firefox_option.headless = self.HEADLESS
        return firefox_option

    @property
    def browser(self):
        """
        启动firefox浏览器并进行初始配置
        :return:
        """
        if self.GRID_MARK:  # 判断是否启动GRID
            if self.OPTION_MARK:  # 判断是否执行启动参数
                firefox = self._remote(command_executor=self.COMMAND_EXC,
                                       desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
                                       options=self._options)  # 得到远程chrome浏览器实例
            else:
                firefox = self._remote(command_executor=self.COMMAND_EXC,
                                       desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        else:
            if self.OPTION_MARK:
                firefox = self._driver(executable_path=self._path, options=self._options)  # 得到chrome浏览器实例
            else:
                firefox = self._driver(executable_path=self._path)

        # firefox.implicitly_wait(self.IMPLICITLY_WAIT_TIME)
        if self.METHOD_MARK:
            # firefox.set_page_load_timeout(self.PAGE_LOAD_TIME)
            # firefox.set_script_timeout(self.SCRIPT_TIMEOUT)
            firefox.maximize_window()
            if self.WINDOW_SIZE:
                firefox.set_window_size(*self.WINDOW_SIZE)
        return firefox


class EDGE(Browser):
    OPTION_MARK = EDGE_OPTION_MARK

    METHOD_MARK = EDGE_METHOD_MARK

    WINDOW_SIZE = EDGE_WINDOW_SIZE

    def __init__(self):
        super(EDGE, self).__init__(
            browser_type=Edge,
            option_type=EdgeOptions,
            driver_path=super().EDGE_DRIVER_PATH

        )

    @property
    def _options(self):
        """
        ie浏览器特有的操作属性
        :return:
        """
        edge_option = self._option()
        edge_option.page_load_strategy = 'normal'
        return edge_option

    @property
    def browser(self):
        """
        启动edge浏览器并进行初始配置
        :return:
        """
        if self.GRID_MARK:
            if self.OPTION_MARK:
                edge = self._remote(command_executor=self.COMMAND_EXC,
                                    desired_capabilities=DesiredCapabilities.EDGE.copy(),
                                    options=self._options)
            else:
                edge = self._remote(command_executor=self.COMMAND_EXC,
                                    desired_capabilities=DesiredCapabilities.EDGE.copy())
        else:
            if self.OPTION_MARK:
                edge = self._driver(executable_path=self._path, options=self._options)
            else:
                edge = self._driver(executable_path=self._path)
        if self.METHOD_MARK:
            # edge.set_page_load_timeout(self.PAGE_LOAD_TIME)
            # edge.set_script_timeout(self.SCRIPT_TIMEOUT)
            edge.maximize_window()
            if self.WINDOW_SIZE:
                edge.set_window_size(*self.WINDOW_SIZE)
        return edge


class SAFARI(Browser):
    METHOD_MARK = SAFARI_METHOD_MARK

    WINDOW_SIZE = SAFARI_WINDOW_SIZE

    def __init__(self):
        super(SAFARI, self).__init__(
            browser_type=Safari,
        )

    @property
    def _options(self):
        return

    @property
    def browser(self):
        """
        启动edge浏览器并进行初始配置
        :return:
        """
        logger.info('打开safari浏览器')
        if self.GRID_MARK:
            safari = self._remote(command_executor=self.COMMAND_EXC,
                                  desired_capabilities=DesiredCapabilities.SAFARI.copy())
        else:
            safari = self._driver()
        if self.METHOD_MARK:
            # safari.set_page_load_timeout(self.PAGE_LOAD_TIME)
            safari.set_script_timeout(self.SCRIPT_TIMEOUT)
            safari.maximize_window()
            if self.WINDOW_SIZE:
                safari.set_window_size(*self.WINDOW_SIZE)
        return safari
