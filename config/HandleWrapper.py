"""

define a class and method that returns every possible locator type to locate
objects in your web

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class HandleWrapper():


    def __init__(self,driver):

        self.driver = driver

    # locator type is the type of possible locators that can be used to locate the objects

    def getByType(self,locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":

            return By.ID
        elif locatorType == "xpath":
            return By.XPATH

        elif locatorType == "cssSelector":
            return By.CSS_SELECTOR

        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT

        else:
            print("locator type not supported")


    def getElements(self,locator,locatorType):

       element = None

       try:

           locatorType = locatorType.lower()

           byType = self.getByType(locatorType)

           element = self.driver.find_element(byType,locator)

           print("element found"+ str(element))

       except:
        print("element not found")

        return element







