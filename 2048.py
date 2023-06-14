from random import choice
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

url = "https://play2048.co"

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)
element = driver.find_element(By.TAG_NAME, "body")
for i in range(100):
    keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]
    random_key = choice(keys)
    print(f"Key = {random_key}")
    sleep(0.3)
    element.send_keys(random_key)