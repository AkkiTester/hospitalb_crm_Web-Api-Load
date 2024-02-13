from utilities.generic_func import AutomationClass


class PatientPage(AutomationClass):
    # locator
    textbox_search_patient = [["xpath", "//input[@type='search']"], ["id", "submit"]]

    patientname = 'test2'

    def __init__(self, driver):
        super().__init__(driver)

    def searchPatient(self, patientName):
        self.action('setText', self.textbox_search_patient, patientName)
