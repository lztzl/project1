#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2
# @Author  : Mik

from selenium.webdriver.common.keys import Keys


class KeyEvent(Keys):
    """解包才能用 eg:send_keys(*KeyEvent.COPY)"""
    COPY = Keys.CONTROL, 'c'
    PASTE = Keys.CONTROL, 'v'
