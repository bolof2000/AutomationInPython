from selenium import webdriver
import os


class RunTest():

    def testMethod(self):

       #driver = webdriver.Firefox(executable_path= "/Volumes/SECURE_DATA/TestAutomation/DriverExe/geckodriver")
       driver = webdriver.Firefox()
       driver.get("https://learn.letskodeit.com/p/practice")


run = RunTest()

run.testMethod()


class RunTestChrome():

    def testInchrome(self):
        driverLocation = "/Volumes/SECURE_DATA/TestAutomation/DriverExe/chromedriver"

        os.environ["webdriver.chrome.driver"] = driverLocation

        driver = webdriver.Chrome(driverLocation)


        driver.get("https://learn.letskodeit.com/p/practice")

runChrome = RunTestChrome()
runChrome.testInchrome()
