from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from utilities.browser import capture_screenshot
import pytest
import datetime
import base64
import os




# --------------------------------------------------------------

# Report Title
def pytest_html_report_title(report):
    report.title = "Demo Hospitl CRM Web Application"


#Test case Name
# def pytest_html_results_table_row(report, cells):
#     # Customize the test case name displayed in the HTML report
#     cells[1] = cells[1].split("::")[-1]  # Keep only the last part of the test name (without path)
#     if "parametrize" in report.keywords:
#         # Remove parameters from test case name if parameterized
#         param_str = str(report.keywords["parametrize"].args)
#         cells[1] = cells[1].split("[")[0]


# ---------------------------------------------------------------------------------------------

# This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# @pytest.fixture
# def setup(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching chrome browser.........")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching firefox browser.........")
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#         print("Launching firefox browser.........")
#     else:
#         driver = webdriver.Chrome()
#     yield driver
#     driver.close()

#
# --------------------------------------------ENV Titles---------------------------------------------------
def pytest_configure(config):
    config.stash[metadata_key]["Compony"] = "RemoSys Tech , Pune"
    config.stash[metadata_key]['Project Name'] = 'Demo Hospitl'
    config.stash[metadata_key]['Module Name'] = 'CRM'
    config.stash[metadata_key]['Tester'] = 'Akash Dilwale'


# # -----------------------------Cross Browser Run-----------------------------------------------------
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


# -----------------------------------------Screenshots Funcation -----------------------------------------------------
# directory components ScreenShot
screenshot_folder = 'Screenshot'
# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create a platform-independent file path relative to the current working directory
screenshot_path = os.path.join(current_directory, screenshot_folder)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # ---------------------------------------------
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name= report.nodeid.split("::")[-1]+".png"
            screenshot_path = os.path.join(current_directory, screenshot_folder,file_name)
            capture_screenshot(screenshot_path)
            if screenshot_path:
                with open(screenshot_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                       f'style="width:90%;height:90%;" /><button onclick="window.close()" ' \
                       f'style="position:relative;display: flex;justify-content: center;align-items: center;top:0;right:0;left: 0;bottom: 0;margin: auto;"</div>'
                extra.append(pytest_html.extras.html(html))
        # ---------------------------------------------
        # if (report.skipped and xfail) or (report.failed and not xfail):
        #     file_name = report.nodeid.replace("::", "_") + ".png"
        #     screenshot_path = os.path.join(current_directory, directory, file_name)
        #     # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
        #     _capture_screenshot(file_name)
        #     if file_name:
        #         # Convert screenshot to base64 and embed it in the HTML
        #         # with open(file_name, "rb") as image_file:
        #         #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        #         # html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
        #         #        f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
        #         #        f'style="position:absolute;top:0;right:0;z-index:9999;"</div>'
        #         with open(file_name, "rb") as image_file:
        #             encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        #         html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
        #                f'style="width:90%;height:90%;" /><button onclick="window.close()" ' \
        #                f'style="position:relative;display: flex;justify-content: center;align-items: center;top:0;right:0;left: 0;bottom: 0;margin: auto;"</div>'
        #         # with open(file_name, "rb") as image_file:
        #         #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        #         # html = f'<div class="logwrapper">' \
        #         #        f'<div class="logexpander"></div>' \
        #         #        f'<div class="log">' \
        #         #        f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
        #         #        f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
        #         #        f'style="position:absolute;top:0;right:0;z-index:9999;"></div>' \
        #         #        f'</div>' \
        #         #        f'</div>'
        #         extra.append(pytest_html.extras.html(html))
        report.extra = extra
