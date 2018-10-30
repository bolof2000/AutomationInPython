from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import selenium


class loginPageObject():

    def __init__(self,driver):

        self.driver = driver

        self.driver = webdriver.Firefox()
        baseurl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseurl)


        #define variables for all the locators


    loginLink = "Login"
    usernameLoginBox = "user_email"
    passwordLoginBox = "user_password"
    loginButtonLink = "submit"

     #define methods to return the web elements

    def getLoginLink(self):

        self.driver.find_element(By.LINK_TEXT,self.loginLink)

    def getUsernameBox(self):

        self.driver.find_element(By.ID,self.usernameLoginBox)

    def getPasswordLoginBox(self):
        self.driver.find_element(By.ID,self.passwordLoginBox)

    def getLoginButtonLink(self):

        self.driver.find_element(By.LINK_TEXT,self.loginButtonLink)


    #define functions for all the operations

    def ClickLoginLink(self):

        self.getLoginLink().click()

    def sendUsername(self,email):

        self.getUsernameBox().send_keys(email)

    def sendPassword(self,password):

        self.getPasswordLoginBox().send_keys(password)

    def clickLoginButton(self):

        self.getLoginButtonLink().click()


    def loginTest(self,username,password):

        self.clickLoginButton()
        self.sendUsername()
        self.sendPassword()
        self.clickLoginButton()











