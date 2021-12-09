class LogoutPage:
    from selenium.webdriver.common.by import By
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a>i')
    TITLE_TEXT = (By.CSS_SELECTOR, 'div h2')
    def __init__(self, browser):
        self.browser = browser
    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_TEXT).text
    def isLogoutButtonDisplayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()
    def clickLogoutButton(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

