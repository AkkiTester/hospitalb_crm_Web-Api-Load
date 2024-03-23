from utilities.browser import setup
from utilities.readconfig import Readconfig
from pageObject.loginPage import LoginPage
from utilities.customLogger import LogGen
from pageObject.loginPagewithGenricMethods import LoginPageGenric
import pytest
from utilities.My_Report_Data_Main import ReportData


class Test_Login_Func:
    baseURL = Readconfig.geturl()
    username = Readconfig.getid()
    password = Readconfig.getfpassword()
    logger = LogGen.loggen()



    @pytest.mark.regression
    def test_01_admin_login(self, setup):
        self.Report = ReportData()
        self.Report.SetTestCaseName('Verify admin login',Severity='High',Priority='High')
        self.logger.info("Test_001_Login-Admin ")
        self.driver = setup
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("Navigating to Login Page")
        self.Report.SetTestCaseLog('INFO','Navigating to Login Page')
        self.lpg.getUrl(self.baseURL)
        self.logger.info("Entering ID and Password ")
        self.Report.SetTestCaseLog('INFO', 'Entering ID and Password ')
        self.lpg.setUserName(self.username)
        self.lpg.setPassword(self.password)
        self.logger.info("Click on Login Button")
        self.Report.SetTestCaseLog('INFO', 'Click on Login Button')
        self.lpg.clickLogin()
        result = self.driver.current_url
        if "login" in result:
            self.logger.info("Test_001_Login-Admin- fail")
            self.Report.SetTestCaseLog('INFO', 'Admin login Fail ')

            assert False
        else:
            self.Report.SetTestCaseLog('INFO', 'Admin Sucssesfuly login ')
            self.logger.info("Test_001_Login-Admin - Pass ")
            self.Report.SetTestResult(True)
            assert True

# @pytest.mark.skip(reason="reason for skipping the test case")
    # def test_admin_login_TC_01(self, setup):
    #     self.logger.info("Test_001_Login-Admin ")
    #     self.driver = setup
    #     self.logger.info("Navigating to Login Page")
    #     self.driver.get(self.baseURL)
    #     self.lp = LoginPage(self.driver)
    #     self.logger.info("Entering ID and Password ")
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.logger.info("Click on Login Button")
    #     self.lp.clickLogin()
    #     result = self.driver.current_url
    #     if "login" not in result:
    #         self.logger.info("Test_001_Login-Admin- Fail ")
    #         assert False
    #     else:
    #         self.logger.info("Test_001_Login-Admin - Pass ")
    #         assert True
