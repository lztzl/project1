#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 
# @Author  : Mik
import pytest
from common.browser import CHROME, FIREFOX, IE, SAFARI, EDGE
from setting import IMG_PATH, LOG_PATH
from utils.logs import logger
from utils.clear import clear_img, clear_log

_driver = None

_browser = {
    'chrome': CHROME,
    'firefox': FIREFOX,
    'safari': SAFARI,
    'ie': IE,
    'edge': EDGE
}


def pytest_addoption(parser):
    """添加命令行参数--browser"""
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["firefox", "chrome", "safari", "ie", "edge"],
        help="browser option: firefox,chrome,ie,safari,edge"
    )


logger.info('开始清理截图和日志文件...')
clear_img(IMG_PATH)
clear_log(LOG_PATH)


# scope='session'
@pytest.fixture()
def driver(request):
    """定义全局driver参数"""
    global _driver
    bs_name = request.config.getoption("--browser")
    if _driver is None:
        try:
            _driver = _browser[bs_name]().browser
        except Exception:
            logger.exception('打开浏览器失败！')
            raise

    # def fn():
    #     print("当全部用例执行完之后：teardown quit driver！")
    #     _driver.quit()
    #     logger.info('关闭浏览器')
    #
    # request.addfinalizer(fn)
    yield _driver
    logger.info('关闭浏览器,并重置driver')
    _driver.quit()
    _driver = None


@pytest.fixture(autouse=True)
def test_cases_log(request):
    case_name = request.function.__name__
    logger.info(f'*************** 开始执行用例：{case_name} ***************')
    yield
    logger.info(f'*************** 结束执行用例：{case_name} ***************')
