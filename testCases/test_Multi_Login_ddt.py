import pytest
from utilities.browser import setup
from pageObject.loginPagewithGenricMethods import LoginPageGenric
from utilities.readconfig import Readconfig
from utilities.customLogger import LogGen
from utilities import readExcel


class Test_DDT_Login:
    baseURL = Readconfig.geturl()
    path = "C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx"
    logger = LogGen.loggen()  # Logger
    # @pytest.mark.skip('Skiping ')
    @pytest.mark.parametrize(('user', 'passw'), readExcel.alldata(path, 'LDS'))
    def test_login_ddt_001(self, setup, user, passw):
        self.logger.info(f"******* Starting Test_DDT_Login {user} Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPageGenric(self.driver)
        self.lp.setUserName(user)
        self.lp.setPassword(passw)
        self.lp.clickLogin()
        a=True
        try:
            if self.driver.find_element("xpath", "//h1[normalize-space()='Demo Hospital Statistics']").is_displayed():
                self.logger.info(f"****Starting Login {user} Test passed ****")
            # time.sleep(2)
                self.lp.clickLogout()
        except:
            self.logger.info(f"**** Starting Login {user} TestFails ****")
            a = False
        assert a