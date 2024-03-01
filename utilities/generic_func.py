from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Example usage:
# Initialize your automation class
# your_automation = YourAutomationClass(driver)
#
# # click
# your_automation.action('click', locatorList, args)

class AutomationClass:
    def __init__(self, driver):
        self.driver = driver

    def action(self, action: str, locator: list =[], *args, **kwargs):
        """
        Perform various Selenium actions such as click, get text, or wait for an element to be clickable.

        Parameters:
            action (str): The action to perform ('click', 'text', 'element_to_be_clickable').
            locator (list) : Locator For Self Healing
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the action performed.
            :param action:
            :param locator:
        """
        if locator is None:
            locator = []
        driver = self.driver  # assuming self.driver is accessible
        if action == 'geturl':  # Get URL
            driver.get(args[0])
        elif action == 'click':  # Click
            element = self.find_element_with_self_healing(list(locator))
            element.click()
        # elif action == 'click':  # Click
        #     element = driver.find_element(args[0], args[1])
        #     element.click()
        elif action == 'setText':  # Set Text
            element = self.find_element_with_self_healing(list(locator))
            element.clear()
            element.send_keys(args[0])
        # elif action == 'setText':  # Set Text
        #     element = driver.find_element(args[0], args[1])
        #     element.clear()
        #     element.send_keys(args[2])
        elif action == 'switchWindow':  # Windows Switch
            driver.switch_to.window(args[0])
        elif action == 'scroll':  # Scroll
            element = driver.find_element(args[0], args[1])
            driver.execute_script("arguments[0].scrollIntoView();", element)
        elif action == 'implicitly_wait':
            driver.implicitly_wait(args[0])
        elif action == 'click_element_to_be_clickable':
            element = WebDriverWait(driver, args[0]).until(EC.element_to_be_clickable(args[1]))
            element.click()
        elif action == 'text':
            element = driver.find_element(*args)
            return element.text
        elif action == 'element_to_be_clickable10sec':
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(args[0]))
        else:
            raise ValueError("Invalid action provided")

#--------------------------------Self Healing Method------------------------------------
    def find_element_with_self_healing(self, locators):
        """
        Self Healing Method
        Parameters:
            locator (list) : Locator For Self Healing
        :param locators:
        :return element:
        """
        driver = self.driver
        for locator in list(locators):
            try:
                if locator[0] == 'id':
                    element = driver.find_element(By.ID, locator[1])
                elif locator[0] == 'name':
                    element = driver.find_element(By.NAME, locator[1])
                elif locator[0] == 'class':
                    element = driver.find_element(By.CLASS_NAME, locator[1])
                elif locator[0] == 'xpath':
                    element = driver.find_element(By.XPATH, locator[1])
                elif locator[0] == 'css':
                    element = driver.find_element(By.CSS_SELECTOR, locator[1])
                elif locator[0] == 'link_text':
                    element = driver.find_element(By.LINK_TEXT, locator[1])
                elif locator[0] == 'partial_link_text':
                    element = driver.find_element(By.PARTIAL_LINK_TEXT, locator[1])
                elif locator[0] == 'tag':
                    element = driver.find_element(By.TAG_NAME, locator[1])
                else:
                    raise ValueError("Invalid locator type")
                return element
            except NoSuchElementException:
                continue


