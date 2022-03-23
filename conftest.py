#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 
# @Author  : Mik
import pytest
from common.browser import MyChrome, MyFirefox, IE, MySafari, MyEdge
from setting import IMG_PATH, LOG_PATH
from utils.logs import logger
from utils.clear import clear_img, clear_log

_driver = None

_browser = {
    'chrome': MyChrome,
    'firefox': MyFirefox,
    'safari': MySafari,
    'ie': IE,
    'edge': MyEdge
}


def pytest_addoption(parser):
    """添加命令行参数--browser"""
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["firefox", "chrome", "safari", "ie", "edge"],
        help="--browser: firefox,chrome,ie,safari,edge"
    )
    parser.addoption(
        "--grid", action="store", default="0", choices=["0", "1"],
        help="--grid: 1打开grid，0关闭grid"
    )

    parser.addoption(
        "--options", action="store", default=1, choices=['0', '1'],
        help="--options: 0,1 ..."
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
    option_id = int(request.config.getoption("--options"))
    grid = int(request.config.getoption("--grid"))
    if _driver is None:
        try:
            if bs_name == "safari":
                _driver = _browser[bs_name]().browser
            else:
                _driver = _browser[bs_name](grid).browser(option_id)
        except Exception:
            logger.error('打开浏览器失败!')
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
