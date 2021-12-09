class KeyPressesPage:
    from selenium.webdriver.common.by import By

    TITLE_TEXT = (By.CSS_SELECTOR, 'div h3')
    DESCRIBE_TEXT = (By.CSS_SELECTOR, 'div>p:nth-child(2)')
    GREEN_TEXT = (By.CSS_SELECTOR, "[id='result']")
    INPUT_FIELD = (By.CSS_SELECTOR, '[id="target"]')
    # URL
    URL = 'https://the-internet.herokuapp.com/key_presses'
    def __init__(self, browser):
        self.browser = browser
    def loadPage(self):
        self.browser.get(self.URL)
    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_TEXT).text
    def getDescribeText(self):
        return self.browser.find_element(*self.DESCRIBE_TEXT).text
    def isInputFieldDisplayed(self):
        return self.browser.find_element(*self.INPUT_FIELD).is_displayed()
    def clickInputField(self):
        self.browser.find_element(*self.INPUT_FIELD).click()
    def isGreenTextDisplayed(self):
        return self.browser.find_element(*self.GREEN_TEXT).is_displayed()
    def inputOnPage(self):
        self.browser.find_element(*self.INPUT_FIELD).send_keys('a')
    def getGreenText(self):
        return  self.browser.find_element(*self.GREEN_TEXT).text
