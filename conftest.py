import pytest
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

@pytest.fixture()
def browser():
    # se deschide tabul de chrome
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    # return the webdriver instance
    yield driver
    sleep(1)
    driver.quit()
