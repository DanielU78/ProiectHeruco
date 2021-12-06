from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome('c:/chromedriver.exe')
# select an option and verify that is displayed
driver.get('https://the-internet.herokuapp.com/dropdown')
sleep(1)
select = driver.find_element(By.ID, "dropdown")
select.click()
sleep(1)
btn1 = driver.find_element(By.CSS_SELECTOR, 'div>select>option:nth-child(2)')
btn2 = driver.find_element(By.CSS_SELECTOR, 'div>select>option:nth-child(3)')
btn1.click()
sleep(1)
assert btn1.is_displayed() is True
sleep(1)
select = driver.find_element(By.ID, "dropdown")
sleep(1)
select.click()
sleep(1)
btn2.click()
assert btn2.is_displayed() is True
sleep(2)
driver.close()
