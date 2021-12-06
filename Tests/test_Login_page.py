from Pages.Login_page import LoginPage
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_page_is_correct(browser):
    login_page = LoginPage(browser)
    #load the page
    login_page.loadPage()
    #check if title is correct
    assert login_page.getTitlePage() == "Login Page", "Title Error"
def test_description_text_is_displayed(browser):
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    #check if description text is displayed
    assert login_page.getDescribeText() == "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages."
def test_input_username_is_displayed(browser):
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    #check if input username fied is displayed
    assert login_page.isInputUsernameDisplayed() == True, "The username field is not displayed"
def test_input_password_is_displayed(browser):
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    # check if input password fied is displayed
    assert login_page.isInputPasswordDisplayed() == True, "The password field is not displayed"
def test_login_button_is_displayed(browser):
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    # check if login button is displayed
    assert login_page.isLoginButtonDisplayed() == True, "Login button is not displayed"
def test_flash_error_message_is_displayed(browser):
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    #input incorect username and see if a flash message apear
    login_page.InputUsername()
    login_page.clickLoginButton()
    sleep(1)
    assert login_page.isFlashMessageDisplayed() == True, "Flash message is not displayed"