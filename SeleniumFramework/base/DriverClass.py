from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebdriverClass():
    def getWebDriver(self, browserName):
        driver = None
        service_obj = Service()
        if browserName == "chrome":
            driver = webdriver.Chrome(service=service_obj)
        else:
            print("Non c'è un webdriver")

