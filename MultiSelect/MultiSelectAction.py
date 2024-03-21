import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dummypoint.com/seleniumtemplate.html")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID, "multiselect")))

ms_options = Select(ele)

print("Check whether it is a multi select or not : ", ms_options.is_multiple)

ms_v = ms_options.options
for ms_value in ms_v:
    print(ms_value.text)

ms_options.select_by_index(1)
ms_options.select_by_value("mOptionsTwo")
ms_options.select_by_visible_text("mOption3")

time.sleep(2)

ms_options.deselect_by_index(1)
time.sleep(2)

ms_options.deselect_by_value("mOptionTwo")
time.sleep(2)

ms_options.deselect_by_visible_text("mOption2")
time.sleep(2)

time.sleep(2)

ms_options.deselect_all()


input()
