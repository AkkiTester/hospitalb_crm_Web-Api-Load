from utilities.browser import setup
from utilities.readconfig import Readconfig
from pageObject.loginPage import LoginPage
from utilities.customLogger import LogGen
from pageObject.loginPagewithGenricMethods import LoginPageGenric
from pageObject.dashboardpage import DashbordPage
from pageObject.PatientListPage import PatientPage
from utilities.generic_func import AutomationClass
import pytest
from utilities.My_Report_Data_Main import ReportData


class Test_Patien_Func:
    baseURL = Readconfig.geturl()
    username = Readconfig.getid()
    password = Readconfig.getfpassword()
    logger = LogGen.loggen()

    def test_03_SearchPatient(self,setup):
        self.R=ReportData()
        self.R.SetTestCaseName('Test Search Patient Func',Severity='Mediuam',Priority='High')
        self.logger.info("Test_Search_Patient Start")
        self.R.SetTestCaseLog('INFO','Test_Search_Patient Start')
        self.driver = setup
        self.ac = AutomationClass(self.driver)
        self.ac.action('implicitly_wait', [], 2)
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("Navigating to Login Page")
        self.R.SetTestCaseLog('INFO', 'Navigating to Login Page')
        self.lpg.getUrl(self.baseURL)
        self.logger.info("Entering ID and Password and login")
        self.R.SetTestCaseLog('INFO', 'Entering ID and Password and login')
        self.lpg.loginfullstep(self.username, self.password)
        self.logger.info("Click on patient page")
        self.R.SetTestCaseLog('INFO', 'Click on patient page')
        self.dp = DashbordPage(self.driver)
        self.dp.clickpatientmenuoption()
        self.logger.info("Searching patient")
        self.R.SetTestCaseLog('INFO', 'Searching patient')
        self.pp = PatientPage(self.driver)
        A=True
        try:
            self.pp.searchPatient("abcdef")
            element = self.driver.find_element('xpath',"//td[normalize-space()='abcdef']")
            self.logger.info("Test_patient_Serach - pass")
            self.R.SetTestCaseLog('INFO', 'Test Patient Serach - Pass')
            self.R.SetTestResult(True)
        except :
            self.logger.info("Test_patient_Serach - fail ")
            self.R.SetTestCaseLog('INFO', 'Test Patient Serach - Fail')
            A=False
        if A:

            assert True
        else:
            assert False

    Rr = ReportData()
    Rr.SetTestCaseName('Test Search Patient Func 2',Skip=True, Severity='Mediuam', Priority='High',SkipResone='skipping test Reason')
    @pytest.mark.skip(reason="skipping the test case")
    def test_04_SearchPatient(self,setup):
        self.Rr = ReportData()
        self.Rr.SetTestCaseName('Test Search Patient Func 2', Severity='Mediuam', Priority='High')
        self.logger.info("Test_Search_Patient")
        self.driver = setup
        self.Rr.SetTestCaseLog('INFO', 'Test Search Patient 2 Start')
        self.ac = AutomationClass(self.driver)
        self.ac.action('implicitly_wait', [], 2)
        self.lpg = LoginPageGenric(self.driver)
        self.logger.info("Navigating to Login Page")
        self.Rr.SetTestCaseLog('INFO', 'Navigating to Login Page')
        self.lpg.getUrl(self.baseURL)
        self.logger.info("Entering ID, Password and login ")
        self.Rr.SetTestCaseLog('INFO', 'Entering ID and Password and login')
        self.lpg.loginfullstep(self.username, self.password)
        self.logger.info("Click on patient page")
        self.Rr.SetTestCaseLog('INFO', 'Click on patient page')
        self.dp = DashbordPage(self.driver)
        self.dp.clickpatientmenuoption()
        self.logger.info("Searching patient page")
        self.Rr.SetTestCaseLog('INFO', 'Searching patient page')
        self.pp = PatientPage(self.driver)

        try:
            self.pp.searchPatient(self.pp.patientname)
            element = self.driver.find_element('xpath',f"//td[normalize-space()='{self.pp.patientname}']")
            self.logger.info("Test_patient_Serach - pass")
            self.Rr.SetTestCaseLog('INFO', 'Test Patient Serach 2- Pass')
            self.R.SetTestResult(True)
            # Assert that the element is displayed
            assert element.is_displayed(), "Element is not displayed"
        except :
            self.logger.info("Test_patient_serach - fail ")
            self.Rr.SetTestCaseLog('INFO', 'Test Patient Serach 2- Fail')
            assert False

# def test_patient_list_display_url_TC_04(self, setup):
    #     self.logger.info("Test_patient_list_display URL Test Start")
    #     self.driver = setup
    #     self.ac= AutomationClass(self.driver)
    #     self.ac.action('implicitly_wait',[],2)
    #     self.lpg = LoginPageGenric(self.driver)
    #     self.logger.info("Navigating to Login Page ")
    #     self.lpg.getUrl(self.baseURL)
    #     self.logger.info("Entering ID and Password and login and click on Login Button")
    #     self.lpg.loginfullstep(self.username, self.password)
    #     self.logger.info("Click on patient page menu")
    #     self.dp = DashbordPage(self.driver)
    #     self.dp.clickpatientmenuoption()
    #     result = self.driver.current_url
    #     if "patient" in result:
    #         self.logger.info("Test_patient_list_display_url - Pass")
    #         assert True
    #     else:
    #         self.logger.info("Test_patient_list_display_Url - fail")
    #         assert False
