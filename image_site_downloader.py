from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

url = "https://wall.alphacoders.com"
text_string = "bocchi"
driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)
try:
    searchBox = driver.find_element(By.CLASS_NAME, "search-bar.form-control.input-lg")
    searchBox.send_keys(text_string)
    searchBox.submit()
    
except:
    print("No such element of class: search-bar form-control input-lg")