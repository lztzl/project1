#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 
# @Author  : Mik

# 项目地址
# 项目包和文件夹的路径
# 浏览器对象属性
# 测试套件
import os
from os.path import dirname, join

# ---------------------项目地址---------------------
# 项目一地址,迈腾会采项目
PROJECT_01_URL = 'https://maitenghuicai.com'

# 项目二地址
PROJECT_QQ_URL = ''

# 项目三地址
PROJECT_DEMO_URL = ''
# ---------------------项目地址---------------------


# ---------------------项目包和文件夹的路径---------------------
# 项目根目录
BASE_PATH = dirname(__file__).replace(r'\/'.replace(os.sep, ''), os.sep)
SEP = os.sep

# 浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}chromedriver')
EDGE_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}edge_driver')
FIREFOX_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}geckodriver')
IE_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}IEDriverServer')
OPERA_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}opera_driver')

# log路径
LOG_PATH = join(BASE_PATH, f'log{SEP}')

# 截图路径
IMG_PATH = join(BASE_PATH, f'imgs{SEP}')

# 测试数据根路径
DATA_ROOT_PATH = f'{BASE_PATH}{SEP}data{SEP}'

# 数据库配置文件路径
DATABASE_INI_PATH = join(BASE_PATH, f'config{SEP}database.ini')

# ---------------------项目包和文件夹的路径---------------------


# ---------------------浏览器对象共有属性---------------------
# 浏览器基本属性

# 设置显示等待时间
TIMEOUT = 10

# 开启grid开关
GRID_MARK = False

# grid启动url
COMMAND_EXC = 'http://localhost:4444/wd/hub'

# ---------CHROME浏览器特有属性--------

# chrome浏览器启动操作开关
CHROME_METHOD_MARK = True

# chrome启动参数开关
CHROME_OPTION_MARK = True

# 无头化参数
CHROME_HEADLESS = False

# 配置是否保存密码
CHROME_PREFS = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_settings.popups": 0  # 禁用下载弹窗
}

# chrome实验性质启动参数
CHROME_EXPERIMENTAL = {
    # 'mobileEmulation': {'deviceName': 'iPhone 6'},  # 设置手机模式
    'excludeSwitches': ['enable-automation'],  # 反爬设置
}

# ---------CHROME浏览器属性--------


# ---------IE浏览器属性--------

# IE浏览器启动操作开关
IE_METHOD_MARK = True

# ie浏览器启动参数开关
IE_OPTION_MARK = True

# ie浏览器清空本地会话
IE_CLEAN_SESSION = True

# ie页面超时时间
IE_ATTACH_TIMEOUT = 10000

# chrome窗口大小启动参数
IE_WINDOW_SIZE = None  # (1920,1024)

# ---------IE浏览器属性--------


# ---------FIREFOX浏览器属性--------
# FIREFOX浏览器启动操作开关
FIREFOX_METHOD_MARK = True

# FIREFOX浏览器启动参数开关
FIREFOX_OPTION_MARK = True

# FIREFOX无头化参数
FIREFOX_HEADLESS = False

# FIREFOX窗口大小启动参数
FIREFOX_WINDOW_SIZE = None  # (1920,1024)
# ---------FIREFOX浏览器属性--------


# ---------EDGE浏览器属性--------
# EDGE浏览器启动操作开关
EDGE_METHOD_MARK = True

# FIREFOX浏览器启动参数开关
EDGE_OPTION_MARK = True

# FIREFOX窗口大小启动参数
EDGE_WINDOW_SIZE = None  # (1920,1024)
# ---------FIREFOX浏览器属性--------


# ---------SAFARI浏览器属性--------
# EDGE浏览器启动操作开关
SAFARI_METHOD_MARK = True

# FIREFOX窗口大小启动参数
SAFARI_WINDOW_SIZE = None  # (1920,1024)
# ---------SAFARI浏览器属性--------

# ---------------------浏览器对象属性---------------------
