# pip install -U selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://en.wikipedia.org/wiki/Selenium')

# Retrieve single element
some_element = driver.find_element(By.XPATH, 'INSERT_XPATH_HERE')
print(some_element.text)

# Retrieve multiple elements of the same tag
links = driver.find_elements(By.TAG_NAME, 'a')
new_links = [l.get_attribute('href') for l in links]
print(new_links[:10])