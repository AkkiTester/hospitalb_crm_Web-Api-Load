from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import pytest
import datetime
import base64
import os


#--------------------------------------------------------------

# Report Title
def pytest_html_report_title(report):
    report.title = "Demo Hospitl CRM Web Application"


# -------------------------------------------Single Browser Run---------------------------------------------------------

# This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

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
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.close()


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

def pytest_configure(config):
    config.stash[metadata_key]["Compony"] = "RemoSys Tech , Pune"
    config.stash[metadata_key]['Project Name'] = 'Demo Hospitl'
    config.stash[metadata_key]['Module Name']='CRM'
    config.stash[metadata_key]['Tester']='Akash Dilwale'
#
#
#
#
#
# # -----------------------------Cross Browser Run-----------------------------------------------------
# @pytest.fixture(params=["chrome", "firefox","edge"],scope="module")
# def setup(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#         print("Launching chrome browser.........")
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     elif request.param == "edge":
#         driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(4)
#     yield driver
#     driver.close()


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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                # html = f'<div><img src="./{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                #        f'onclick="window.open(this.src)" align="right"/></div>'
                # Convert screenshot to base64 and embed it in the HTML
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                # Convert screenshot to base64 and embed it in the HTML
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:304px;height:228px;" onclick="window.open(\'data:image/png;base64,{encoded_string}\')" align="right"/></div>'
                # Convert screenshot to base64 and embed it in the HTML
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:304px;height:228px;" onclick="openImage(\'{quote(encoded_string)}\')" align="right"/></div>'
                # Convert screenshot to base64 and embed it in the HTML
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:100%;height:auto; cursor:pointer;" ' \
                #        f'onclick="openImage(\'{encoded_string}\')" align="right"/></div>'
                # Convert screenshot to base64 and embed it in the HTML
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
                #        f'style="position:absolute;top:0;right:0;z-index:9999;">Close</button></div>'
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:100%;height:auto;" /><button onclick="closeImageWindow()" ' \
                #        f'style="position:absolute;top:0;right:0;z-index:9999;">Close</button></div>'
                # Convert screenshot to base64 and embed it in the HTML
                with open(file_name, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                       f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
                       f'style="position:absolute;top:0;right:0;z-index:9999;"</div>'
                # with open(file_name, "rb") as image_file:
                #     encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                # html = f'<div class="logwrapper">' \
                #        f'<div class="logexpander"></div>' \
                #        f'<div class="log">' \
                #        f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                #        f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
                #        f'style="position:absolute;top:0;right:0;z-index:9999;"></div>' \
                #        f'</div>' \
                #        f'</div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# Open image in new tab
# @pytest.mark.hookwrapper
# def openImage(encoded_string):
#     js_script = f"window.open('data:image/png;base64,{encoded_string}', '_blank')"
#     yield
#     driver.execute_script(js_script)

# @pytest.mark.hookwrapper
# def openImage(encoded_string):
#     js_script = f'''
#     var imgWindow = window.open("", "Image", "width=800,height=600");
#     imgWindow.document.write('<button onclick="window.close()">Close</button>');
#     imgWindow.document.write('<img src="data:image/png;base64,{encoded_string}" style="width:100%;height:auto;">');
#     '''
#     yield
#     driver.execute_script(js_script)
