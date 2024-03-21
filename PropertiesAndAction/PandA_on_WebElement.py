import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dummypoint.com/seleniumtemplate.html")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()
time.sleep(2)

#wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
#ele = wait.until(ec.presence_of_element_located((By.ID, "user_input")))

ele = driver .find_element(By.ID, "user_input")

ele_d = ele.is_displayed()
print("IS DISPLAYED: ", ele_d)

ele_e = ele.is_enabled()
print("IS ENABLED: ", ele_e)

ele_s = ele.size
print("SIZE OF ELE: ", ele_s)

ele_l = ele.location
print("ELE LOCATION: ", ele_l)

ele.click()

ele.send_keys("Mattia Esposito")
time.sleep(2)

ele.clear()
time.sleep(2)

ele.send_keys("Mattia Esposito seconda volta")
time.sleep(2)

ele_t = ele.get_attribute("value")
print("Text from edit box: ", ele_t)

time.sleep(5)
input()
