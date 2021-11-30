from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('c:/chromedriver.exe')
# Logare pe site
driver.get('https://the-internet.herokuapp.com/login')
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
sleep(2)
username.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
sleep(2)
password.send_keys('SuperSecretPassword!')
login = driver.find_element(By.CSS_SELECTOR, 'button[class]')
login.click()
# verificati ca s-a facut logare cu success 3 aserturi
# 1.
secure_area1_message = driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
assert secure_area1_message.is_displayed() is True, "Login error 1"
# 2.
logout_btn = driver.find_element(By.CSS_SELECTOR, 'div>a>i')
assert logout_btn.is_displayed() is True, "Login error 2"
# 3.
secure_area2_message = driver.find_element(By.CSS_SELECTOR, 'div>h4')
assert secure_area2_message.is_displayed() is True, "Login error 3"
sleep(1)
logout_btn.click()

# logati-va cu un username gresit -> verificati textul de la eroare
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
username.send_keys('tomsmith1')
login = driver.find_element(By.CSS_SELECTOR, 'button[class]')
login.click()
username_error = driver.find_element(By.CSS_SELECTOR, 'div#flash')
assert username_error.is_displayed() is True

# logati-va cu parola gresita -> verificati textul de la eroare
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
sleep(2)
username.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
sleep(2)
password.send_keys('SuperSecretPassword')
login = driver.find_element(By.CSS_SELECTOR, 'button[class]')
login.click()
sleep(1)
password_error = driver.find_element(By.CSS_SELECTOR, 'div#flash')
assert password_error.is_displayed() is True

# logati-va, click logout - >
# 4 aserturi (unul ca linkul pe care va redirectioneaza e ok, altul ca butonul de Login va apare ,
# verificare ca va apare mesajul cu verde, si inca unul
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
sleep(2)
username.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
sleep(2)
password.send_keys('SuperSecretPassword!')
login = driver.find_element(By.CSS_SELECTOR, 'button[class]')
login.click()
logout_btn = driver.find_element(By.CSS_SELECTOR, 'div>a>i')
logout_btn.click()
sleep(2)
# verificare redirectionare pe linkul de login
login_page = driver.find_element(By.CSS_SELECTOR, 'div>h2')
assert login_page.is_displayed() is True
# verificare existenta buton de login
login = driver.find_element(By.CSS_SELECTOR, 'button[class]')
assert login.is_displayed() is True
# verificare existenta mesaj de logout
secure_area1_message = driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
assert secure_area1_message.is_displayed() is True
# verificare existenta campurilor de input user si parola
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
assert username.is_displayed() is True
password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
assert password.is_displayed() is True
driver.close()
