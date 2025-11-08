import logging
from selenium.webdriver.common.by import By
from Utilitis.LogUtil import Logger
from Utilitis import ConfigReader

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_RESOURCEID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).click()
        log.logger.info(f"Clicking on an element {locator}")

    def click_index(self, locator,index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_RESOURCEID"):
            self.driver.find_elements(By.ID, ConfigReader.readConfig("locators", locator))[index].click()
        log.logger.info(f"Clicking on an element {locator} with index {index}")

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_RESOURCEID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info(f"Typing on an element {locator} Enter the value as {value}")

    def get_text(self, locator):
        global text
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_RESOURCEID"):
            text = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).text
        log.logger.info(f"getting text from an element {locator}")
        return text
