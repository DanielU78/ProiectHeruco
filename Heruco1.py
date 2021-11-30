from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def test_add_element(): # testam ca dam click pe add element
    driver = webdriver.Chrome('c:/chromedriver.exe')
    sleep(2)
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    title = driver.find_element(By.CSS_SELECTOR, 'div h3')
    assert title.text =="Add/Remove Elements", "Error"
    driver.quit()

def test_add_element(): # testam ca dam click pe add element
    driver = webdriver.Chrome('c:/chromedriver.exe')
    sleep(2)
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add_button = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')

# testul care verifica si ca nu mai apare butonul de delete
# ca un element nu e visibil se poate verifica asa cum am facut aici cu verificare
# ca lista care ar trebui sa gaseasca elementele e goala
def test_add_element():
    driver = webdriver.Chrome('C:/chromedriver.exe')
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    # click add element
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()
    sleep(4)
    #check delete button is displayed
    delete_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert delete_button.is_displayed() is True, "Delete button is not displayed"
    delete_button.click()
    sleep(5)
    list = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert len(list) == 0, "Delete button is displayed"
    driver.quit()