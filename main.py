from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys

chrome_driver_path = os.environ.get("DRIVER_PATH")
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

driver.get("https://tinder.com/")
login = driver.find_element(By.XPATH, '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q-405061102"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys(email)
password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_location = driver.find_element(By.XPATH, '//*[@id="q-405061102"]/div/div/div/div/div[3]/button[1]/span')
allow_location.click()

not_notifications = driver.find_element(By.XPATH, '//*[@id="q-405061102"]/div/div/div/div/div[3]/button[2]/span')
not_notifications.click()

allow_cookies = driver.find_element(By.XPATH, '//*[@id="q1323319974"]/div/div[2]/div/div/div[1]/button/span')
allow_cookies.click()

for n in range(100):
    time.sleep(5)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        like_button = driver.find_element(By.XPATH, '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

driver.quit()

# driver.set_window_size(1280, 800)
