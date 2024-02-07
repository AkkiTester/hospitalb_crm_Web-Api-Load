from selenium import webdriver
import pytest
import datetime
import os





# Report Title
def pytest_html_report_title(report):
    report.title = "Demo Hospitl CRM Web Application"


# -------------------------------------------Single Browser Run---------------------------------------------------------

# This will get the value from CLI /hooks
# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture(scope='session', autouse=True)
# def setup(request):
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
#         driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(4)
#     yield driver
#     driver.close()


# -----------------------------------------------------------main code ende---------------------------------------------------


# # @pytest.fixture()
# # def browser(request):  # This will return the Browser value to setup method
# #     return request.config.getoption("--browser")
# #########pytest HTML##############
# def pytest_configure(config):
#     config._metadata['Project Name']='Demo Hospitl'
#     config._metadata['Module Name']='CRM'
#     config._metadata['Tester']='Akash Dilwale'
#
#
#
#
#
#
# # -----------------------------Cross Browser Run-----------------------------------------------------
@pytest.fixture(params=["chrome", "firefox","edge"],scope="module")
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.close()


# ----------------------------------------------------------------------------------------------------------------

#----------------------------------------Pending ---------------------
# from selenium import webdriver
# import pytest
#
# driver = None
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if True: #(report.skipped and xfail) or (report.failed and not xfail)
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

