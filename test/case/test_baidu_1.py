import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import configs, DRIVER_PATH
from utils.log import logger


class TestBaiDu:
    URL = configs['URL']
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.get(self.URL)

    def teardown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('爱你 python3')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('爱你 test')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu_1.py'])