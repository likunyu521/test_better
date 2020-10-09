import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import configs, DRIVER_PATH,DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader

class TestBaiDu:
    URL = configs['URL']
    excel = DATA_PATH + '/baidu.xlsx'
    datas = ExcelReader(excel).data
    params= []
    for data in datas:
        a = list(data.values())[0]
        params.append(a)

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
    # params = ['selenium 灰蓝', 'Python selenium']

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.get(self.URL)

    def teardown(self):
        self.driver.quit()


    @pytest.mark.parametrize("search_value", params) # 调用pytest参数化用例接口
    def test_search(self,search_value):
        self.driver.find_element(*self.locator_kw).send_keys(search_value)
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu_params.py'])