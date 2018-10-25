from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

class SeleniumDriver():

    def __init__(self,driver):

        self.driver = driver

    def getType(self,locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID

        elif locatorType == "name":
            return By.NAME

        elif locatorType == "xpath":
            return By.XPATH

        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME

        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("locator type"+locatorType+ "not correct/supported")
        return False




