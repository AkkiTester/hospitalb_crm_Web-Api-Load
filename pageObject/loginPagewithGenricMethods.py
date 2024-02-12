from utilities.generic_func import AutomationClass


class LoginPageGenric(AutomationClass):
    # locator
    textbox_username_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@type='submit']"
    link_logout_ = ""

    def __init__(self, driver):
        super().__init__(driver)

    def getUrl(self,URL):
        self.action('geturl',URL)

    def setUserName(self, username):
        self.action('setText','xpath',self.textbox_username_xpath,username)

    def setPassword(self, password):
        self.action('setText', 'xpath', self.textbox_password_xpath, password)

    def clickLogin(self):
        self.action('click','xpath',self.button_login_xpath)


    def clickLogout(self):
        pass

    def loginfullstep(self,username,password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()
