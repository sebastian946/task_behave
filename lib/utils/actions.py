
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def waitElementPresent(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    def openUrl(self,url):
        self.driver.get(url)

    def clickElement(self,locator:WebElement):
        by, value = locator
        self.waitElementPresent(locator)
        self.driver.find_element(by,value).click()

    def sendKeys(self,locator:WebElement,send:str):
        by, value = locator
        self.waitElementPresent(locator)
        self.driver.find_element(by,value).send_keys(send)

    def getContextText(self,locator):
        by,value = locator
        self.waitElementPresent(locator)
        return self.driver.find_element(by,value).text

    def waitSecond(self,seconds):
        self.driver.implicitly_wait(seconds)