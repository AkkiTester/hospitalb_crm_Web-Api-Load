from selenium.webdriver.common.by import By


class LoginPage:
    # locator
    textbox_username_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@type='submit']"
    link_logout_ = ""

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        # self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        pass

    def loginfullsteep(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.button_login_xpath()