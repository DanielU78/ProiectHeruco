from Pages.Key_Presses_page import KeyPressesPage
from selenium.webdriver.common.keys import Keys
from time import sleep
def test_page_is_correct(browser):
    key_presses_page = KeyPressesPage(browser)
    # load the page
    key_presses_page.loadPage()
    # check the title is correct
    assert key_presses_page.getTitlePage() == 'Key Presses', 'Title is not correct'
def test_describe_text_is_displayed(browser):
    key_presses_page = KeyPressesPage(browser)
    # load the page
    key_presses_page.loadPage()
    # testam existenta textului de descriere
    assert key_presses_page.getDescribeText() == 'Key presses are often used to interact with a website (e.g., tab order, enter, escape, etc.). Press a key and see what you inputted.'
def test_input_field_is_displayed(browser):
    key_presses_page = KeyPressesPage(browser)
    # load the page
    key_presses_page.loadPage()
    # testam existenta campului de input
    assert key_presses_page.isInputFieldDisplayed() == True, "Error"
def test_key_presses_function(browser):
    key_presses_page = KeyPressesPage(browser)
    # load the page
    key_presses_page.loadPage()
    # apasam tasta "a" si verificam aparitia textului cu verde
    key_presses_page.inputOnPage()
    sleep(1)
    assert key_presses_page.isGreenTextDisplayed() == True, "Error Green Text"
def test_green_text_is_correct_displayed(browser):
    key_presses_page = KeyPressesPage(browser)
    # load the page
    key_presses_page.loadPage()
    # apasam tasta "a" si verificam daca corespunde cu tasta care am apasat-o
    key_presses_page.inputOnPage()
    assert key_presses_page.getGreenText() == 'You entered: A', 'Error Text'
