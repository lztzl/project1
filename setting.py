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
SEP = os.sep  # 路径分隔符

# 浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}chromedriver')
EDGE_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}edge_driver')
FIREFOX_DRIVER_PATH = join(BASE_PATH, f'drivers{SEP}geckodriver.exe')
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


# ---------------------浏览器对象属性---------------------

# 显示等待时间
TIMEOUT = 10

# 开启grid开关
GRID_MARK = True

# grid启动url
COMMAND_REMOTE_EXECUTOR = 'http://81.68.118.175:4444/wd/hub'

FIREFOX_SERVICE_LOG_PATH = LOG_PATH+"server.log"

# ---------------------浏览器对象属性---------------------
