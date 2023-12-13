from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Define Chrome WebDriver options
chrome_options = Options()
service = Service('/Users/mac005/Downloads/chromedriver-mac-arm64/chromedriver')

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
# Open the Flask application
driver.get('http://192.168.105.15:3000')  

# Find input fields and perform addition
number_one_input = driver.find_element(By.NAME, 'number_one')
number_two_input = driver.find_element(By.NAME, 'number_two')
operation_select = driver.find_element(By.NAME, 'operation')
submit_button = driver.find_element(By.ID, 'calc_btn')

# Enter numbers and select addition operation
number_one_input.send_keys('10')
number_two_input.send_keys('20')
operation_select.send_keys('subtract')

# Click the submit button
submit_button.click()

# Wait for the result (let's say for 3 seconds)
time.sleep(10)

# Get the result element and print the text (replace 'result_id' with your actual result element ID)
result_element = driver.find_element(By.CSS_SELECTOR, 'h3')
print('Result of addition:', result_element.text)

# Close the browser window
driver.quit()
