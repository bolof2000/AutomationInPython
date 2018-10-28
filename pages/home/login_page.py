from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium


class Login_Page():

    def __init__(self,driver):

        self.driver = driver

        driver.get("https://learn.letskodeit.com/p/practice")



    #defind the locators for the login page

    login_link = "login"
    email_field = "user_email"
    password_field = "user_password"
    login_button = "commit"


    #defind methods to return the locator after finding them

    def getLoginLink(self):

        
        return self.driver.find_element(By.LINK_TEXT,self.login_link)

    def getEmailField(self):

        return self.driver.find_element(By.ID,self.email_field)

    def getPasswordField(self):

        return self.driver.find_element(By.ID,self.password_field)

    def getLoginButton(self):

        return self.driver.find_element(By.NAME,self.login_button)



     #define functions for every operations on the login page
     # send username
    #send password
    #click submit button

    def sendUsername(self,email):
        self.getEmailField().send_keys(email)

    def sendPassword(self,password):
        self.getPasswordField().send_keys(password)

    def clickSubitButton(self):

        self.getLoginButton().click()

    def clickLoginLink(self):

        self.getLoginLink().click()


    def loginTest(self,email,password):
        self.clickLoginLink()
        self.sendUsername(email)
        self.sendPassword(password)
        self.clickSubitButton()










