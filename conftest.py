import pytest
import datetime
import os


@pytest.fixture(scope='session', autouse=True)
def html_report_timestamp(request):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join('Reports', 'html-Histroy', f'test_report_{timestamp}.html')
    request.config.option.htmlpath = output_file