from utilities.browser import setup
from utilities.readconfig import Readconfig
from pageObject.loginPage import LoginPage
from utilities.customLogger import LogGen
from pageObject.loginPagewithGenricMethods import LoginPageGenric
from pageObject.dashboardpage import DashbordPage
from pageObject.PatientListPage import PatientPage
from utilities.generic_func import AutomationClass
import pytest


class Test_Patien_Func:
    baseURL = Readconfig.geturl()
    username = Readconfig.getid()
    password = Readconfig.getfpassword()
    logger = LogGen.loggen()

    def test_patient_list_display_url_001(self, setup):
        self.logger.info("*************** Test_patient_list_display *****************")
        self.driver = setup
        self.ac= AutomationClass(self.driver)
        self.ac.action('implicitly_wait',[],2)
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("*************** Navigating to Login *****************")
        self.lpg.getUrl(self.baseURL)
        self.logger.info("*************** Entering ID and Password and login *****************")
        self.lpg.loginfullstep(self.username, self.password)
        self.logger.info("*************** Click on patient page *****************")
        self.dp = DashbordPage(self.driver)
        self.dp.clickpatientmenuoption()
        result = self.driver.current_url
        if "patient" in result:
            self.logger.info("*************** Test_patient_list_display - Pass  *****************")
            assert True
        else:
            self.logger.info("*************** Test_patient_list_display - fail *****************")
            assert False

    def test_SearchPatient__002(self,setup):
        self.logger.info("*************** Test_SearchPatient *****************")
        self.driver = setup
        self.ac = AutomationClass(self.driver)
        self.ac.action('implicitly_wait', [], 2)
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("*************** Navigating to Login *****************")
        self.lpg.getUrl(self.baseURL)
        self.logger.info("*************** Entering ID and Password and login *****************")
        self.lpg.loginfullstep(self.username, self.password)
        self.logger.info("*************** Click on patient page *****************")
        self.dp = DashbordPage(self.driver)
        self.dp.clickpatientmenuoption()
        self.logger.info("*************** Searching patient page *****************")
        self.pp = PatientPage(self.driver)

        try:
            self.pp.searchPatient("abcdef")
            element = self.driver.find_element('xpath',"//td[normalize-space()='abcdef']")
            self.logger.info("*************** Test_patient_list_display - pass*****************")
            # Assert that the element is displayed
            element.is_displayed()
            assert True #"Element is not displayed"
        except :
            self.logger.info("*************** Test_patient_list_display - fail *****************")
            assert False

    def test_SearchPatient_003(self,setup):
        self.logger.info("*************** Test_SearchPatient *****************")
        self.driver = setup
        self.ac = AutomationClass(self.driver)
        self.ac.action('implicitly_wait', [], 2)
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("*************** Navigating to Login *****************")
        self.lpg.getUrl(self.baseURL)
        self.logger.info("*************** Entering ID and Password and login *****************")
        self.lpg.loginfullstep(self.username, self.password)
        self.logger.info("*************** Click on patient page *****************")
        self.dp = DashbordPage(self.driver)
        self.dp.clickpatientmenuoption()
        self.logger.info("*************** Searching patient page *****************")
        self.pp = PatientPage(self.driver)

        try:
            self.pp.searchPatient(self.pp.patientname)
            element = self.driver.find_element('xpath',f"//td[normalize-space()='{self.pp.patientname}']")
            self.logger.info("*************** Test_patient_list_display - pass*****************")
            # Assert that the element is displayed
            assert element.is_displayed(), "Element is not displayed"
            print("Assertion passed: Element with text 'test2' is displayed")
        except :
            self.logger.info("*************** Test_patient_list_display - fail *****************")
            print("Assertion failed: Element with text 'test2' not found")
            assert False

