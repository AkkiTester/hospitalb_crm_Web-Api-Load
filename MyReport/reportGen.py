import json
import platform

import jinja2
from jinja2 import Environment, FileSystemLoader

# Report Data file saved in a Dict Variable
with open("report_data.json", "r") as f:
    report_data = json.load(f)

# Calculate the total number of tests and the number of passed tests
total_tests = len(report_data)
passed_tests = sum(1 for test in report_data.values() if test["Result"] == True)
Skipped_tests = sum(1 for test in report_data.values() if test["Skipped"] == True)



# Pass the calculated values to the template
env = Environment(loader=FileSystemLoader('./Template'))
template = env.get_template("index.html")

rendered_html = template.render(test_cases=report_data,
                                passed_tests=passed_tests,
                                total_tests=total_tests,
                                Skipped_tests=Skipped_tests,
                                platform=platform.platform())



with open("report.html", "w") as f:
    f.write(rendered_html)
