import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dummypoint.com/Windows.html")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Form")))

wait.until(ec.presence_of_element_located((By.NAME, "promtalertb"))).click()
time.sleep(2)

a_button = Alert(driver)

time.sleep(2)
print(a_button.text)
a_button.send_keys("MattiaEsposito")
a_button.accept()
