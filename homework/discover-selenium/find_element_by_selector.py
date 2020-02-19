import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.TAG_NAME, 'input')
    first_name.send_keys('Ivan')
    
    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')

    city_info = browser.find_element(By.CLASS_NAME, 'city')
    city_info.send_keys('Smolensk')

    country_info = browser.find_element(By.ID, 'country')
    country_info.send_keys('Russia')

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()

