from utilities.generic_func import AutomationClass


class LoginPageGenric(AutomationClass):
    # locator
    textbox_username = [["xpath", "//input[@name='email']"], ["id", "submit"]]
    textbox_password = [["xpath", "//input[@name='password']"], ["id", "submit"]]
    button_login = [["id", "submit"], ["xpath", "//input[@type='submit']"]]
    link_logout_ = ""

    def __init__(self, driver):
        super().__init__(driver)

    def getUrl(self, URL):
        self.action('geturl', [], URL)

    def setUserName(self, username):
        self.action('setText', self.textbox_username, username)

    def setPassword(self, password):
        self.action('setText', self.textbox_password, password)

    def clickLogin(self):
        self.action('click', self.button_login)

    def clickLogout(self):
        pass

    def loginfullstep(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()
