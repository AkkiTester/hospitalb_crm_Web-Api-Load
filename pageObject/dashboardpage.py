from utilities.generic_func import AutomationClass


class DashbordPage(AutomationClass):
    # locator
    patient_menu_option = [["xpath","//a[normalize-space()='Patient']"],["id","akash"]]

    def __init__(self, driver):
        super().__init__(driver)

    def clickpatientmenuoption(self):
        self.action('click',self.patient_menu_option)
