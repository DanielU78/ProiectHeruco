from pages.Logout_page import LogoutPage
from pages.Login_page import LoginPage
from time import sleep

def test_click_logout_button(browser):
    logout_page = LogoutPage(browser)
    login_page = LoginPage(browser)
    # load the page
    login_page.loadPage()
    sleep(1)
    # login on the page
    login_page.typeUsername("tomsmith")
    login_page.typePassword("SuperSecretPassword!")
    login_page.clickLoginButton()
    sleep(1)
    # verify if describe text is displayed
    assert logout_page.isDescribeTextDisplayed() == 'Welcome to the Secure Area. When you are done click logout below.'
    # click on logout button
    logout_page.clickLogoutButton()
    # verify if you have return on login page
    assert login_page.getTitlePage() == 'Login Page'

