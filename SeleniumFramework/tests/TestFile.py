from selenium.webdriver.common.by import By
from SeleniumFramework.base.DriverClass import WebdriverClass
import time

wd = WebdriverClass()
driver = wd.getWebDriver("chrome")
driver.get("https://dummypoint.com/seleniumtemplate.html")
driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()
time.sleep(2)


time.sleep(2)
input()