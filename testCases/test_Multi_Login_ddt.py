import os
import pytest
from utilities.browser import setup
from pageObject.loginPagewithGenricMethods import LoginPageGenric
from utilities.readconfig import Readconfig
from utilities.customLogger import LogGen
from utilities import readExcel

# directory components
directory = 'TestData'
filename = 'Logindata.xlsx'

# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a platform-independent file path relative to the current working directory
file_path = os.path.join(current_directory, directory,filename)

class Test_DDT_Login:
    baseURL = Readconfig.geturl()
    path = file_path #"C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx"
    logger = LogGen.loggen()  # Logger
    # @pytest.mark.skip('Skiping ')
    @pytest.mark.parametrize(('user', 'passw'), readExcel.alldata(path, 'LDS'))
    def test_02_login_ddt(self, setup, user, passw,request):
        self.logger.info(f"Starting Test_DDT_Login {user} Test")
        self.logger.info("Navigating Login DDT Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPageGenric(self.driver)
        self.logger.info("Entering ID and Password ")
        self.lp.setUserName(user)
        self.lp.setPassword(passw)
        self.logger.info("Click on Login Button")
        self.lp.clickLogin()
        a=True
        try:
            if self.driver.find_element("xpath", "//h1[normalize-space()='Demo Hospital Statistics']").is_displayed():
                self.logger.info(f"Login {user} User is successfully logged in to the app")
            # time.sleep(2)
                self.lp.clickLogout()
        except:
            self.logger.info(f"Login {user} Invalid user login : Username/Password is incorrect ")
            a = False
        assert a