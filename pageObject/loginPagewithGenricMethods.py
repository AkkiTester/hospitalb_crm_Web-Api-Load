from utilities.generic_func import AutomationClass


class LoginPageGenric(AutomationClass):
    # locator
    textbox_username = [["id", "akash"], ["xpath", "//input[@name='email']"],["id", "submit"]]
    textbox_password = [["xpath", "//input[@name='password']"], ["id", "submit"]]
    button_login = [ ["xpath", "//input[@type='submit']"] , ["id", "submit"]]
    link_logout = [['xpath',"//a[@class='dropdown-toggle']"],['xpath',"//a[normalize-space()='Sign out']"],["id", "submit"]]
    signout = [['xpath',"//a[normalize-space()='Sign out']"],['xpath',"//a[normalize-space()='Sign out']"]]

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
        self.action('click',self.link_logout)
        self.action('click',self.signout)
    def loginfullstep(self, username, password):
        self.action('setText', self.textbox_username, username)
        self.action('setText', self.textbox_password, password)
        self.clickLogin()
