from utilities.generic_func import AutomationClass


class DashbordPage(AutomationClass):
    # locator
    patient_menu_option_xpath = "//a[normalize-space()='Patient']"

    def __init__(self, driver):
        super().__init__(driver)

    def clickpatientmenuoption(self):
        self.action('click', 'xpath', self.patient_menu_option_xpath)
