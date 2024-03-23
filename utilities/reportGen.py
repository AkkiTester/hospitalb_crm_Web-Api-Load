import json
import os
import platform
import pytest
from jinja2 import Environment, FileSystemLoader

directory = 'Reports'
filename = 'HTMLReport.html'
dir = 'utilities'
dir2 = 'Template'
ffile='index.html'
# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a platform-independent file path relative to the current working directory
file_pathhr = os.path.join(current_directory, directory, filename)
file_pathhi = os.path.join(current_directory, dir, dir2 )

def generate_report(report_data):
    print(file_pathhi)
    total_tests = len(report_data)
    passed_tests = sum(1 for test in report_data.values() if test["Result"] == True)
    Skipped_tests = sum(1 for test in report_data.values() if test["Skipped"] == True)

    env = Environment(loader=FileSystemLoader(file_pathhi))
    template = env.get_template('index.html')

    rendered_html = template.render(test_cases=report_data,
                                    passed_tests=passed_tests,
                                    total_tests=total_tests,
                                    Skipped_tests=Skipped_tests,
                                    platform=platform.platform(),
                                    reportname='Demo Hospital CRM Web Application')

    with open(file_pathhr, "w") as f:
        f.write(rendered_html)
