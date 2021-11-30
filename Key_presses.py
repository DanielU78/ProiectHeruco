from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome('c:/chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/key_presses?')
sleep(1)

# apasati enter si verificati mesajul cu verde ce va apare
page = driver.find_element(By.CLASS_NAME, 'no-js')
page.send_keys(Keys.ENTER)
sleep(1)
msg = driver.find_element(By.ID, 'result')
assert msg.is_displayed() is True
sleep(1)
driver.close()
