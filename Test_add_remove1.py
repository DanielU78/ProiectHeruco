from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('c:/chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
# dati de doua ori click pe butonul de click -> verificati ca va apar doua butoane
add_button = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
sleep(1)
add_button.click()
sleep(1)
add_button.click()
sleep(1)
del_btn2 = driver.find_element(By.CSS_SELECTOR, 'div>button:nth-child(2)')
assert del_btn2.is_displayed() is True, "The second button is not displayed"
# stergeti un buton  -> verificati ca va apare doar unul
del_btn2.click()
assert del_btn2.is_displayed(), not True
del_btn1 = driver.find_element(By.CSS_SELECTOR, 'div>button:nth-child(1)')
assert del_btn1.is_displayed() is True
driver.close()
