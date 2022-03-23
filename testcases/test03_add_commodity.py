import allure

from utils.logs import logs
from pom.add_commodity import AddCommodity
import time


@allure.epic('Web测试')
@allure.severity('blocker')
@allure.feature('购物流程')
class TestComm:
    def setup(self):
        pass

    def teardown(self):
        time.sleep(3)

    @allure.story('正常购物')
    @allure.title('测试数据')
    @logs
    def test01(self, driver):
        page = AddCommodity(driver)
        page.add_comm()
