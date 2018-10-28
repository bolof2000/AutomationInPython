"""
This is the page object model for the login page
every object locators, objects and the functionalities are defined in this class



"""

from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class LoginPageModel():


    def __init__(self,driver):

        baseurl = "https://learn.letskodeit.com/p/practice0"

        self.driver = driver

        self.driver = webdriver.Firefox()

        self.driver.get(baseurl)
        self.driver.maximize_window()

    login_link = "login"
    email_field = "user_email"
    password_field = "user_password"
    login_button = "commit"



    #define locators as variable



    def getLoginLink(self):

        return self.driver.find_element(By.LINK_TEXT,self.login_link)

    def getUsernameBox(self):

        return self.driver.find_element(By.ID,self.email_field)

    def getPasswordBox(self):

        return self.driver.find_element(By.ID,self.password_field)

    def getLoginButton(self):

        return self.driver.find_element(By.ID,self.login_button)


    # define functions for all operations

    def sendUsername(self,email):

        self.getUsernameBox().send_keys(email)

    def sendPassword(self,password):

        self.getPasswordBox().send_keys(password)

    def clickLoginLinkButton(self):

        self.getLoginLink().click()

    def clickLoginButton(self):

        self.getLoginButton().click()



    def login(self,email,password):

        self.clickLoginLinkButton()
        self.clickLoginButton()
        self.sendUsername("bolofindeolusegun@gmail.com")
        self.sendPassword("bolofbaba")



