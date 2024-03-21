import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dummypoint.com/seleniumtemplate.html")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()

assert "Selenium Template — DummyPoint" in driver.title
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()


input()
