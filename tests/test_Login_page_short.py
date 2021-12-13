from pages.Login_page import LoginPage
from pages.Logout_page import LogoutPage
from time import sleep

def test_page_is_correct(browser):
    login_page = LoginPage(browser)
    logout_page = LogoutPage(browser)
    # load the page
    login_page.loadPage()
    # check if title is correct
    assert login_page.getTitlePage() == "Login Page", "Title Error"
    sleep(1)
    # check if description text is displayed
    assert login_page.getDescribeText() == "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages."
    sleep(1)
    # check if input username field is displayed
    assert login_page.isInputUsernameDisplayed() == True, "The username field is not displayed"
    sleep(1)
    # check if input password field is displayed
    assert login_page.isInputPasswordDisplayed() == True, "The password field is not displayed"
    sleep(1)
    # check if login button is displayed
    assert login_page.isLoginButtonDisplayed() == True, "Login button is not displayed"
    sleep(1)
    # input incorrect username and see if a flash message appear
    login_page.typeUsername("Ion")
    login_page.clickLoginButton()
    sleep(1)
    assert login_page.isFlashMessageDisplayed() == True, "Flash message is not displayed"
    sleep(1)
def test_login_succesfully(browser):
    login_page = LoginPage(browser)
    logout_page = LogoutPage(browser)
    # load the page
    login_page.loadPage()
    # input correct username and password
    login_page.typeUsername("tomsmith")
    login_page.typePassword("SuperSecretPassword!")
    login_page.clickLoginButton()
    sleep(1)
    # verify if login is succesfully, check title
    assert logout_page.getTitlePage() == 'Secure Area', "The title is not correct"
    sleep(2)



