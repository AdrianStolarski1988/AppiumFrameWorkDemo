import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.CustomLogger as cl

class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locator_value: str, locator_type: str):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 NoSuchElementException])
        if locator_type == "id":
            element = wait.until(lambda x: x.find_element_by_id(locator_value))
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locator_value))
            return element
        elif locator_type == "des":
            element = wait.until(lambda x: x.find_element_by_andoroid_uiautomator(f'UiSelector().description("{locator_value}")'))
            return element
        elif locator_type == "index":
            element = wait.until(lambda x: x.find_element_by_andoroid_uiautomator("UiSelector().index(%d)" % int(locator_value)))
            return element
        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator(f'UiSelector().text("{locator_value}")'))
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath(f'{locator_value}'))
            return element
        else:
            self.log.info(f"Locator value '{locator_value}' not found")
            self.takeScreenshot(locator_type)

        return element

    def getElement(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitForElement(locator_value, locator_type)
            self.log.info(f"Element found with LocatorType: '{locator_type}' with the locatorValue '{locator_value}'")
        except:
            self.log.info(f"Element not found with LocatorType: '{locator_type}' with the locatorValue '{locator_value}'")
            self.takeScreenshot(locator_type)
            assert False

        return element

    def clickElement(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitForElement(locator_value, locator_type)
            element.click()
            self.log.info(f"Clicked on Element with LocatorType: '{locator_type}' and with the locatorValue '{locator_value}'")
        except:
            self.log.info(
                f"Unable to click on Element with LocatorType: '{locator_type}' and with the locatorValue '{locator_value}'")
            self.takeScreenshot(locator_type)
            assert False

    def sendText(self, text, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitForElement(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(f"Send text on Element with LocatorType: '{locator_type}' and with the locatorValue '{locator_value}'")
        except:
            self.log.info(
                f"Unable to send text on Element with LocatorType: '{locator_type}' and with the locatorValue '{locator_value}'")
            self.takeScreenshot(locator_type)
            assert False

    def isDisplayed(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitForElement(locator_value, locator_type)
            element.is_displayed()
            self.log.info(
                f"Element with LocatorType: {locator_type} and with the locatorValue {locator_value} is displayed")
            return True
        except:
            self.log.info(
                f"Element with LocatorType: {locator_type} and with the locatorValue {locator_value} is not displayed")
            self.takeScreenshot(locator_type)
            return False

    def screenshot(self, screenshot_name):
        fileName  = screenshot_name + str(time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshot_directory = "../screenshots/"
        screenshot_path = screenshot_directory + fileName
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info(f'Screenshot save to path : {str(screenshot_path)}')
        except:
            self.log.info(f'Unable to save screenshot to the path : {str(screenshot_path)}')

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)