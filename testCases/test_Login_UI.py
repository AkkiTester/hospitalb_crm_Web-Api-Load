from utilities.readconfig import Readconfig
from pageObject.loginPage import LoginPage
from utilities.customLogger import LogGen
from pageObject.loginPagewithGenricMethods import LoginPageGenric
import pytest


class Test_Login_Func:
    baseURL = Readconfig.geturl()
    username = Readconfig.getid()
    password = Readconfig.getfpassword()
    logger = LogGen.loggen()

    @pytest.mark.skip(reason="reason for skipping the test case")
    def test_admin_login001(self, setup):
        self.logger.info("*************** Test_001_Login-Admin *****************")
        self.driver = setup
        self.logger.info("*************** Navigating to Login *****************")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("*************** Entering ID and Password *****************")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("*************** Click on Login *****************")
        self.lp.clickLogin()
        result = self.driver.current_url
        if "login" not in result:
            self.logger.info("*************** Test_001_Login-Admin- fail *****************")
            assert False
        else:
            self.logger.info("*************** Test_001_Login-Admin - Pass *****************")
            assert True

    @pytest.mark.regression
    def test_admin_login_genric_methods002(self, setup):
        self.logger.info("*************** Test_001_Login-Admin *****************")
        self.driver = setup
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("*************** Navigating to Login *****************")
        self.lpg.getUrl(self.baseURL)
        self.logger.info("*************** Entering ID and Password *****************")
        self.lpg.setUserName(self.username)
        self.lpg.setPassword(self.password)
        self.logger.info("*************** Click on Login *****************")
        self.lpg.clickLogin()
        result = self.driver.current_url
        if "login" in result:
            self.logger.info("*************** Test_001_Login-Admin- fail *****************")
            assert False
        else:
            self.logger.info("*************** Test_001_Login-Admin - Pass *****************")
            assert True
