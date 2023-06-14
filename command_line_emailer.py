from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

email = "owaisalikhan2003@gmail.com"

url = "https://www.gmail.com"
driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)
try:
    emailElem = driver.find_element(By.ID, "identifierId")
    emailElem.send_keys(email)

    class_name = "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"
    class_name = class_name.replace(" ", ".")
    nextElem = driver.find_element(By.CLASS_NAME, class_name)
    nextElem.click()
    # emailElem.submit()
except NoSuchElementException:
    print("No element found with id = identifierID")
