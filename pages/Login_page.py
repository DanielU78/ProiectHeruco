class LoginPage:
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    TITLE_TEXT = (By.CSS_SELECTOR, 'div h2')
    DESCRIBE_TEXT = (By.CSS_SELECTOR, 'div>h4')
    INPUT_USERNAME = (By.CSS_SELECTOR, '[id="username"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '[id="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button>i')
    FLASH_MESSAGE = (By.CSS_SELECTOR, '[id="flash"]')

    #URL
    URL = 'https://the-internet.herokuapp.com/login'
    def __init__(self, browser):
        self.browser = browser
    def loadPage(self):
        self.browser.get(self.URL)
    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_TEXT).text
    def getDescribeText(self):
        return self.browser.find_element(*self.DESCRIBE_TEXT).text
    def isInputUsernameDisplayed(self):
        return self.browser.find_element(*self.INPUT_USERNAME).is_displayed()
    def isInputPasswordDisplayed(self):
        return self.browser.find_element(*self.INPUT_PASSWORD).is_displayed()
    def isLoginButtonDisplayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()
    def clickLoginButton(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()
    def typeUsername(self,username):
        self.browser.find_element(*self.INPUT_USERNAME).send_keys(username)
    def isFlashMessageDisplayed(self):
        return self.browser.find_element(*self.FLASH_MESSAGE).is_displayed()
    def typePassword(self,password):
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(password)


