import json
from utilities.reportGen import generate_report
from utilities.My_Report_Data_Main import ReportData
import platform
import re
import sys
import pytest
import pytest_html
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from utilities.browser import capture_screenshot
import pytest
import datetime
import base64
import os
import collections
# from utilities.browser import browserindex

# --------------------------------------------------------------
# Report Title
def pytest_html_report_title(report):
    report.title = "Demo Hospitl CRM Web Application"

# def pytest_html_results_table_html(report, data):
#         a= data
#         # print(a)
#         data.append(a)

# Test case Name
# def pytest_html_results_table_row(report, cells):
#     # Customize the test case name displayed in the HTML report
#     cells[1] = cells[1].split("::")[-1]  # Keep only the last part of the test name (without path)
#     if "parametrize" in report.keywords:
#         # Remove parameters from test case name if parameterized
#         param_str = str(report.keywords["parametrize"].args)
#         cells[1] = cells[1].split("-")[0]

# ---------------------------------------------------------------------------------------------

# This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# --------------------------------------------ENV Titles---------------------------------------------------
#Befor Session Env
# def pytest_configure(config):
#     # Create an OrderedDict for environment data
#     environment_data = collections.OrderedDict()
#     # Add an extra HTML snippet with a link and image
#     environment_data[
#         "Company"] = "<a href='https://remo-sys.com/'><img src='https://img1.wsimg.com/isteam/ip/bd3785cd-d6c4-4882-9b7c-6e71611da2b9/Remosys%20Logo%202.png' width='100' height='100' /></a><br />  RemoSys Tech , Pune"
#     # Add your desired environment information
#     environment_data["Project Name"] = "Demo Hospitl"
#     environment_data["Module Name"] = "CRM"
#     environment_data["Tester"] = "Akash Dilwale"
#     environment_data["Python"]= sys.version[:6]
#     environment_data["Platform"] = platform.platform()
#     # Set the environment data using the metadata key
#     config.stash[metadata_key] = environment_data

#After Session Env
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config.stash[metadata_key]["After Seesion"] ='After Session End'

#after Seesin below Summary
# @pytest.hookimpl()
# def pytest_html_results_summary(prefix, summary, postfix, session):
#     """
#     Modifies the report summary to include test case counts.
#     """
#     failed = session.testsfailed+1
#
#     passed = len(session.session.items) - failed
#
#     # Format the counts and modify the summary
#     summary_text = f"Akash Summary: Passed: {passed}, Failed: {failed}, Skipped:"
#     summary.extend([summary_text])
    # prefixt= type(prefix)
    # print(f"summary type: {type(summary)}")
    # print(f"postfix type: {type(postfix)}")
    # print(f"session type: {type(session)}")

    # summary.extend(prefixt)
    # summary.extend(summary)
    # summary.extend(postfix)
    # summary.extend(session)

    # Return the modified summary
    # return prefix, summary, postfix


# def pytest_html_results_summary(prefix, summary, postfix,session):
#     prefix.extend(["<p>foo: bar</p>"])
#     summary.extend('Akash Summary'+session.passed+session.testsfailed)

# def pytest_html_results_table_html(report, data):
#     data.append(f"<div>Custom information for test: {report.head_line}</div>")
# def pytest_html_results_table_header(cells):
#     cells.insert(2, "<th>Description</th>")
    # cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')

# def pytest_html_results_table_row(report, cells):
#     # Customize the test case name displayed in the HTML report
#     cells[2] = cells[1].split("::")[-1]  # Keep only the last part of the test name (without path)
#     if "parametrize" in report.keywords:
#         # Remove parameters from test case name if parameterized
#         param_str = str(report.keywords["parametrize"].args)
#         cells.insert(2,f'<td {cells[1].split("[")[0]} </td>')

def pytest_html_results_table_row(report, cells):
    if cells[1].count('-') == 0:
        cells[1] = f'<td>{cells[1].split("::")[2]}</td>'

    elif cells[1].count('-') == 1:
        a=(cells[1].split("::")[2]).split("-")[0]
        cells[1] = f'<td>{a}</td>'
        # cells[1] = f'<td>{(cells[1].split("::")[2]).split("-")[0]}</td>'
    else:
        a='-'.join((cells[1].split("::")[2]).split("-")[0:-1])+']'
        cells[1] = f'<td>{a}</td>'
        # a = ((cells[1].split("::")[2]).split("-")[0:-1]) + ']'
        # cells[1] = f'<td>{"".join(a)}</td>'
        # cells[1] = f'<td>{((cells[1].split("::")[2]).split("-")[0:-1])}</td>'

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

# -----------------------------------------Screenshots Funcation -----------------------------------------------------
# directory components ScreenShot
screenshot_folder = 'Screenshot'
# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create a platform-independent file path relative to the current working directory
screenshot_path = os.path.join(current_directory, screenshot_folder)


# This fail - when non web test case fail
# Use - web test fail take screenshot


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
                       f'style="width:50%;height:50%;" /><button onclick="window.close()" ' \
                       f'style="position:relative;display: flex;justify-content: center;align-items: center;top:0;right:0;left: 0;bottom: 0;margin: auto;"</div>'

                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    # Load report data from JSON file
    with open(ReportData.report_file, "r") as f:
        report_data = json.load(f)

    # Generate the report
    generate_report(report_data)