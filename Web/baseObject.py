import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseObject:
    def __init__(self, driver, logger):
        self.driver = driver
        self.base_url = "http://localhost/en-gb?route=common/home"
        self.logger = logger

    def find_element(self, locator, time=10):
        self.logger.info(f"Поиск элементов по локатору: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Нету такого элемента {locator}")

    def find_elements(self, locator, time=10):
        self.logger.info(f"Поиск элементов по локатору: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Нету такого элемента {locator}")

    def go(self):
        return self.driver.get(self.base_url)