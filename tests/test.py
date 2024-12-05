import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from credentials import username, password
import time

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')

driver = webdriver.Chrome(options=options)

try:
    # Navigate to the website
    driver.get('https://game-one-customizer-stg.qstrike.net/')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.title_contains('Game One Customizer - Home'))

    # Click login button
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@class='qx-login']"))).click()

    # Fill in username
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='login-dropdown']/form/div[1]/div/input"))).send_keys(username)
    
    time.sleep(2)
    # Fill in password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='login-dropdown']/form/div[2]/div/div/input"))).send_keys(password)
    
    # Submit the login form
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='login-dropdown']/form/div[3]/button"))).click()
    time.sleep(5)
finally:
    # Stop the driver
    driver.quit()
