import json
import sys
import platform

import jinja2
# Load JSON data from a file
with open("report_data.json", "r") as f:
    report_data = json.load(f)

with open("report_template2.html", "r") as f:
    template = jinja2.Template(f.read())


rendered_html = template.render(data=report_data,html_report_name='Test Report Name',
                                start_datetime='12:00',
                                httprunner_version=platform.version(),
                                python_version=sys.version[:6],
                                platform=platform.platform())
with open("report.html", "w") as f:
    f.write(rendered_html)
