import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
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

assert "Selenium Template — DummyPoint" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Form"))).click()
wait.until(ec.presence_of_element_located((By.ID, "reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.ID, "name"))).send_keys("Mattia Esposito")
wait.until(ec.presence_of_element_located((By.ID, "email"))).send_keys("abc@gmail.com")
wait.until(ec.presence_of_element_located((By.ID, "message"))).send_keys("ABCDEFG")
captcha = wait.until(ec.presence_of_element_located((By.ID, "captcha_image")))
wait.until(ec.presence_of_element_located((By.ID, "captcha"))).send_keys(captcha.text)

postButton = wait.until(ec.presence_of_element_located((By.ID, "btnContactUs")))


actions = ActionChains(driver)
actions.move_to_element(postButton).perform()
postButton.click()



input()
