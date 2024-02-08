from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Example usage:
# Initialize your automation class
# your_automation = YourAutomationClass(driver)
#
# # click
# your_automation.action('click', locatorName, locatorValue)

class AutomationClass:
    def __init__(self, driver):
        self.driver = driver

    def action(self, action, *args, **kwargs):
        """
        Perform various Selenium actions such as click, get text, or wait for an element to be clickable.

        Parameters:
            action (str): The action to perform ('click', 'text', 'element_to_be_clickable').
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the action performed.
        """
        driver = self.driver  # assuming self.driver is accessible
        if action == 'geturl':  # Get URL
            driver.get(args[0])
        elif action == 'click':  # Click
            element = driver.find_element(args[0], args[1])
            element.click()
        elif action == 'setText':  # Set Text
            element = driver.find_element(args[0], args[1])
            element.clear()
            element.send_keys(args[2])
        elif action == 'switchWindow':  # Windows Switch
            driver.switch_to.window(args[0])
        elif action == 'scroll':  # Scroll
            element = driver.find_element(args[0], args[1])
            driver.execute_script("arguments[0].scrollIntoView();", element)
        elif action == 'click_element_to_be_clickable10sec':
            element = WebDriverWait(driver, args[0]).until(EC.element_to_be_clickable(args[1]))
            element.click()
        elif action == 'text':
            element = driver.find_element(*args)
            return element.text
        elif action == 'element_to_be_clickable':
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(args[0]))
        else:
            raise ValueError("Invalid action provided")
