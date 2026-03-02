from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Define Chrome WebDriver options
chrome_options = Options()
service = Service('/Users/mac005/Downloads/chromedriver-mac-arm64/chromedriver')

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Flask application
driver.get('http://192.168.105.23:3000') 

# Find elements and interact with them
search_box = driver.find_element(By.NAME, 'number_one')
search_box.send_keys(100)

search_box = driver.find_element(By.NAME, 'number_two')
search_box.send_keys(145)

search_box = driver.find_element(By.NAME, 'operation')
search_box.send_keys('add')

search_button = driver.find_element(By.ID, 'calc_btn')
search_button.click()

# Wait for an element to appear before performing an action
try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, 'results'))
    )
    print("Results found:", element.text)
except:
    print("Results didn't load")

# Perform assertions to validate UI behavior
assert "Expected Result" in driver.page_source

# Close the browser
driver.quit()
