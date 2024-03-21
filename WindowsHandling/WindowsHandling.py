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
driver.get("https://dummypoint.com/Windows.html")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.LINK_TEXT, "Procedi su dummypoint.com (non sicuro)").click()
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])


window_name = driver.current_window_handle
print("Before switching: " , window_name)

ele = driver.find_elements(By.TAG_NAME, "input")

for popup_bs in ele:
    popup_b = popup_bs.get_attribute("value")
    if popup_b == "Open a Popup Window2":
        popup_bs.click()

time.sleep(2)

windows = driver.window_handles
for window in windows:
    print(window)

driver.switch_to.window(windows[1])

time.sleep(2)
window_name = driver.current_window_handle
print("After switching: " , window_name)

driver.maximize_window()

