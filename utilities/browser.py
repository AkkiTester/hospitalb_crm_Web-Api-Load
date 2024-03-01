from selenium import webdriver
import pytest



# ------------------------------------------Single Browser-----------------------------
@pytest.fixture
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.close()


# -----------------------------Cross Browser Run-----------------------------------------------------
# @pytest.fixture(params=["chrome", "firefox","edge"],scope="module")
# def setup(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#         print("Launching chrome browser.........")
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     elif request.param == "edge":
#         driver = webdriver.Edge()
#     yield driver
#     driver.close()
#-----------------------------------------------------------------------------------------------

def capture_screenshot(name):
    # screenshot_path = os.path.join(current_directory, screenshot_folder, name)
    # driver.get_screenshot_as_file(screenshot_path)
    # Create a platform-independent file path relative to the current working directory
    # screenshot_path = os.path.join(current_directory, directory, name)
    driver.get_screenshot_as_file(name)