#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 
# @Author  : Mik
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.select import Select
from setting import IMG_PATH, TIMEOUT
from typing import Optional, List, Union, Any
from utils.logs import logger
import time
import allure
from enum import Enum


###########################################################
# 基于selenium接口二次封装底层操作类，采用页面描述和元素描述。命名原则尽量不改变原方法名或者见名知其意。
# 操作主要分为常用的浏览器操作，元素操作，鼠标操作，键盘操作，和js操作，需要相应操作可以到对应模块寻找。
#
###########################################################


class BasePage:
    """基于原生selenium第二次封装"""

    def __init__(self, driver: WebDriver):
        """
        页面基类初始化
        :param driver: web driver
        """
        self.driver = driver
        self._timeout = TIMEOUT

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info(f'强制等待{seconds}s')

    # #############浏览器操作部分#############
    def get(self, url: str) -> None:
        """
        Get url
        :param url: 请求地址
        :return: None
        """
        try:
            logger.info(f'导航到:{url}')
            self.driver.get(url)
        except Exception:
            raise

    def find_element(self, locator: Enum) -> WebElement:
        """
        Find the element and return the element
        :param locator: Element enumeration ID
        :return: WebElement
        """
        if not isinstance(locator.value, tuple):
            raise TypeError('args error')
        else:
            try:
                logger.info('定位元素：{}, 元素描述：{}'.format(locator.value, locator))
                start_time = time.time()
                ele = WebDriverWait(self.driver, self._timeout).until(EC.visibility_of_element_located(locator.value))
                end_time = time.time()
            except Exception:
                logger.error('元素定位失败,开始截图!')
                self.save_screenshot()
                raise
            else:
                logger.info('元素定位成功:耗时{}秒!'.format(round(end_time - start_time, 3)))
                return ele

    def find_elements(self, locator: Enum) -> Union[List[WebElement], List]:
        """
        Find the elements and return the elements
        :param locator: Element enumeration ID
        :return: Elements list
        """
        if not isinstance(locator.value, tuple):
            raise TypeError('args error')
        else:
            try:
                logger.info('定位元素:{}, 元素描述:{}'.format(locator.value, locator))
                start_time = time.time()
                eles = WebDriverWait(self.driver, self._timeout).until(
                    EC.visibility_of_all_elements_located(locator.value))
                end_time = time.time()
            except Exception:
                logger.error('元素定位失败,开始截图!')
                self.save_screenshot()
                raise
            else:
                logger.info('元素定位成功：耗时{}秒!'.format(round(end_time - start_time, 3)))
                return eles

    def get_handles(self) -> Union[int, List[Union[int, str]]]:
        """
        获取当前所有句柄
        :return: handles list
        """
        logger.info('获取所有句柄')
        try:
            handles = self.driver.window_handles
        except Exception:
            logger.error('获取所有句柄失败,开始截图!')
            self.save_screenshot()
            raise
        else:
            return handles

    def switch_alert(self, send_keys: Optional[str] = None, accept: bool = True) -> str:
        """
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :param send_keys: 输入内容
        :param accept: 是否接受
        :return: alert text
        """
        try:
            alert = WebDriverWait(self.driver, self._timeout).until(EC.alert_is_present())
            # result = self.driver.switch_to.alert
            if alert and accept:
                text = alert.text
                logger.info("alert出现,内容:{}".format(text))
                alert.accept()
                logger.info("确认并关闭alert")
                return text
            elif alert and not accept:
                text = alert.text
                logger.info("alert出现,内容:{}".format(text))
                alert.dismiss()
                logger.info("取消并关闭alert")
                return text
            elif alert and send_keys:
                text = alert.text
                logger.info("alert出现,内容:{}".format(text))
                alert.send_keys(send_keys)
                alert.accept()
                logger.info(f"输入{send_keys},并确认alert")
                return text
            else:
                logger("alert操作失败")
        except Exception:
            logger.error("goto alert失败,开始截图!")
            self.save_screenshot()
            raise

    def switch_window(self, old_handles: List, handle: str = 'new') -> None:
        """
        窗口切换,默认切换新window,default 切换第一个window。old_handles 打开window之前的所有windiw
        :param handle: (new, default,handle name )
        :param old_handles:切换新打开窗口时传入，传入的句柄为打开新窗口之前的所有句柄
        :return:
        """
        try:
            if handle == "new":
                logger.info("切换到新打开的窗口")
                WebDriverWait(self.driver, self._timeout).until(EC.new_window_is_opened(old_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif handle == "default":
                logger.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
            else:
                logger.info(f"切换到指定{handle}")
                self.driver.switch_to.window(handle)
        except Exception:
            logger.error("window切换失败!,开始截图")
            self.save_screenshot()
            raise

    def switch_iframe(self, locator: Enum) -> None:
        """
        切换frame
        :param locator: 元素定位
        :return:
        """
        try:
            WebDriverWait(self.driver, self._timeout).until(
                EC.frame_to_be_available_and_switch_to_it(locator.value))
            logger.info("frame切换成功")
        except Exception:
            logger.error("frame切换失败,开始截图")
            self.save_screenshot()
            raise

    def save_screenshot(self) -> None:
        """
        窗口截图，并加入allure报告
        :return: None
        """
        name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filepath = f'{IMG_PATH}{name}.png'
        try:
            self.driver.save_screenshot(filepath)
            logger.info("window截屏成功,图片路径为:{}".format(filepath))
            time.sleep(1)
            allure.attach.file(filepath, name, allure.attachment_type.PNG)
        except Exception:
            logger.error("截屏失败")
            raise

    def window_close(self) -> None:
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
        logger.info('关闭窗口')

    def browser_close(self) -> None:
        """
        关闭浏览器
        :return:
        """
        self.driver.close()
        self.driver = None
        logger.info('关闭浏览器')

    # #############元素操作部分#############

    def find_element_and_send_keys(self, locator: Enum, text: str) -> None:
        """
        输入操作
        :param locator:元素定位表达式
        :param text: 输入内容
        :return:
        """
        ele = self.find_element(locator)
        try:
            logger.info('输入内容:"{}", 元素描述:{}'.format(text, locator))
            ele.clear()
            ele.send_keys(text)
        except Exception:
            logger.error('输入失败!,开始截图')
            self.save_screenshot()
            raise

    def find_element_and_click(self, locator: Enum) -> None:
        """
        点击操作
        :param locator:元素定位表达式
        :return: None
        """
        ele = self.find_element(locator=locator)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        if ele.is_enabled():
            ele.click()
            logger.info('点击元素:{}, 元素描述:{}'.format(locator.value, locator))
        else:
            logger.error('点击失败,开始截图')
            self.save_screenshot()
            raise Exception("元素不可点击")

    def find_element_and_screenshot(self, locator: Enum) -> None:
        """
        元素截图
        :return: None
        """
        name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filepath = f'{IMG_PATH}{name}.png'
        ele = self.find_element(locator)
        try:
            ele.screenshot(filepath)
            logger.info("元素截图成功,图片路径为:{}".format(filepath))
            allure.attach.file(filepath, name, allure.attachment_type.PNG)
        except Exception:
            logger.error("元素截图失败")
            raise

    def find_element_and_submit(self, locator: Enum) -> None:
        """
        提交form表单操作，元素定位在form表单中任意元素即可
        记住只能在form表单中使用，一般在submit难定位时使用
        :param locator:元素定位表达式
        :return:
        """
        ele = self.find_element(locator)
        try:
            logger.info('提交form表单')
            ele.submit()
        except Exception:
            logger.error('submit失败')
            self.save_screenshot()
            raise

    def get_text(self, locator: Enum) -> str:
        """
        Get element text
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            text = ele.text
            logger.info('获取文本:"{}", 元素描述：{}'.format(text, locator))
        except Exception:
            logger.error("获取文本失败!")
            self.save_screenshot()
            raise
        else:
            return text

    def uncheck_checkbox(self, locator: Enum) -> None:
        """
        取消选择复选框
        :param locator:
        :return:
        """
        if self.checkbox_status(locator):
            logger.info("取消复选框")
            self.find_element_and_click(locator)
        else:
            logger.info('复选框没有选择')

    def check_checkbox(self, locator: Enum) -> None:
        """
        选择复选框
        :param locator:
        :return:
        """
        if not self.checkbox_status(locator):
            logger.info("选择复选框")
            self.find_element_and_click(locator)
        else:
            logger.info('复选框已是选择')

    def checkbox_status(self, locator: Enum) -> Any:
        """
        Get checkbox status
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            status = ele.is_selected
            logger.info(f"复选框状态：{True}")
            return status
        except Exception:
            logger.error("获取复选框状态失败!")
            self.save_screenshot()
            raise

    def dropdown_select_by_value(self, locator: Enum, value: str) -> None:
        """
        通过属性value值选择下拉框
        :param locator:
        :param value:
        :return:
        """
        ele = self.find_element(locator)
        try:
            logger.info('下拉框选择：{}'.format(value))
            Select(ele).select_by_value(value)
        except Exception:
            logger.exception('下拉框选择失败')
            self.save_screenshot()
            raise

    def dropdown_select_by_text(self, locator: Enum, text: str) -> None:
        """
        通过text选择下拉框
        :param locator:
        :param text:
        :return:
        """
        ele = self.find_element(locator)
        try:
            logger.info('下拉框选择：{}'.format(text))
            Select(ele).select_by_visible_text(text)
        except Exception:
            logger.exception('下拉框选择失败')
            self.save_screenshot()
            raise

    def dropdown_select_by_index(self, locator: Enum, index: int) -> None:
        """
        通过index选择下拉框
        :param locator:
        :param index:
        :return:
        """
        ele = self.find_element(locator)
        try:
            logger.info('下拉框选择：{}'.format(index))
            Select(ele).select_by_index(index)
        except Exception:
            logger.exception('下拉框选择失败')
            self.save_screenshot()
            raise

    def get_attribute(self, locator: Enum, value: str = 'value') -> str:
        """
        get元素属性值，默认get value属性值
        :param locator:
        :param value:
        :return:
        """
        ele = self.find_element(locator)
        try:
            val = ele.get_attribute(value)
            logger.info(f'获取元素属性值：{val}')
            return val
        except Exception:
            logger.Exception('获取属性值失败')
            self.save_screenshot()
            raise

    # #############js操作部分#############
    def click_by_js(self, locator: Enum) -> None:
        """
        通过js点击操作
        :param locator:元素定位表达式
        :return: None
        """
        try:
            logger.info('点击元素:{}, 元素描述:{}'.format(locator.value, locator))
            ele = WebDriverWait(self.driver, self._timeout).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception:
            logger.error('点击失败,元素不可点击或者元素点位失败')
            self.save_screenshot()
            raise

    def scroll_into_view_by_js(self, locator: Enum) -> None:
        """
        滚动到元素可见位置
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            logger.info("滚动到元素：{} ,元素描述：{}".format(locator.value, locator))
        except Exception:
            logger.error("滚动操作失败。")
            self.save_screenshot()
            raise

    # #############鼠标操作部分#############
    def double_click(self, locator: Enum) -> None:
        """
        鼠标双击
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            AC(self.driver).double_click(ele).perform()
            logger.info("双击元素:{}, 元素描述:{}".format(locator.value, locator))
        except Exception:
            logger.error("鼠标双击操作失败!")
            self.save_screenshot()
            raise

    def right_click(self, locator: Enum) -> None:
        """
        鼠标右击
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            AC(self.driver).context_click(ele).perform()
            logger.info("右击元素：{},元素描述:{}".format(locator.value, locator))
        except Exception:
            logger.error("右击操作失败!")
            self.save_screenshot()
            raise

    def drag_and_drop(self, locator_rource: Enum, locator_tarteg: Enum) -> None:
        """
        鼠标拖动元素
        :param locator_rource:
        :param locator_tarteg:
        :return:
        """
        ele = self.find_element(locator_rource, )
        ele1 = self.find_element(locator_tarteg)
        try:
            AC(self.driver).drag_and_drop(ele, ele1).perform()
            logger.info("拖动元素:{}到{}, 元素描述:{}到{}".format(locator_rource.value, locator_tarteg.value, locator_rource,
                                                        locator_tarteg))
        except Exception:
            logger.error("拖动操作失败!")
            self.save_screenshot()
            raise

    def mouse_hover(self, locator: Enum) -> None:
        """
        鼠标悬停到元素位置
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        try:
            AC(self.driver).move_to_element(ele).perform()
            logger.info("鼠标悬停：{}, 元素描述:{}".format(locator.value, locator))
        except Exception:
            logger.error("鼠标操作失败!")
            self.save_screenshot()
            raise

    # #############键盘操作部分#############
    def key_down(self, key: str, text: str) -> None:
        """
        用于模拟按下辅助按键(CONTROL, SHIFT, ALT)的动作，按住。光标处于可输入状态
        :param key: 键盘操作码
        :param text: 输入值
        :return:
        """
        # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
        try:
            logger.info('按住{}输入{}'.format(key, text))
            AC(self.driver).key_down(key).send_keys(text).perform()
        except Exception:
            logger.error('输入失败')
            self.save_screenshot()
            raise

    def key_up(self, locator: Enum, key: str, text: str, key1: str, text1: str) -> None:
        """
        用于模拟辅助按键(CONTROL, SHIFT, ALT)弹起或释放的操作，松开
        :param key:按住键
        :param locator:定位器
        :param text:输入文本
        :param key1:松开键
        :param text1:输入文本
        :return:
        """
        # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
        ele = self.find_element(locator)
        try:
            logger.info('输入内容：{}{}'.format(text, text1))
            ele.clear()
            AC(self.driver).key_down(key).send_keys_to_element(ele, text).key_up(key1).send_keys(text1).perform()
        except Exception:
            logger.error('输入失败!')
            self.save_screenshot()
            raise
