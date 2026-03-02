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
driver.get('http://192.168.105.23:3000')  

number1 = driver.find_element(By.NAME, 'number_one')
number2 = driver.find_element(By.NAME, 'number_two')
operator = driver.find_element(By.NAME, 'operation')
submit = driver.find_element(By.ID, 'calc_btn')

number1.send_keys(12)
number2.send_keys(-3)
operator.send_keys('divide')

submit.click()

time.sleep(3)

result = driver.find_element(By.CSS_SELECTOR, 'h3')
print("Result is: ", result.text)

number1 = driver.find_element(By.NAME, 'number_one')
number2 = driver.find_element(By.NAME, 'number_two')
operator = driver.find_element(By.NAME, 'operation')
submit = driver.find_element(By.ID, 'calc_btn')

number1.send_keys(-12)
number2.send_keys(3)
operator.send_keys('divide')

submit.click()

time.sleep(3)

result = driver.find_element(By.CSS_SELECTOR, 'h3')
print("Result is: ", result.text)


driver.close()