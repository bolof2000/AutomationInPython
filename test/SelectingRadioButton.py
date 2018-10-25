from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time


class WebElementlists():



    def WebelementLists(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        radioButtonList = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/fieldset/legend")

        # radiobutton is a list of web elements

        for radioButton in radioButtonList:

            selectedButton = radioButton.is_selected()

            if not selectedButton:

                radioButton.click()
                time.sleep(10)


