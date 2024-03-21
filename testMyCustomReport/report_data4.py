import datetime
import json
import threading

class ReportData:
    TestAllData = {}
    lock = threading.Lock()
    report_file = 'report_data.json'


    def __init__(self):
        self.TestName = ''

    def SetTestCaseName(self, TestName):
        self.TestName = TestName
        with self.lock:
            self.TestAllData[TestName] = {'log': [],
                                           'StartTime': datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p"),
                                           'EndTime': datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p"),
                                           'Result': False}
        self._save_to_json()

    def SetTestCaseLog(self, LogType, LogMessage):
        log_entry = [datetime.datetime.now().strftime("%I:%M:%S %p"), LogType, LogMessage]
        with self.lock:
            self.TestAllData[self.TestName]['log'].append(log_entry)
            self.TestAllData[self.TestName]['EndTime'] = datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p")
        self._save_to_json()

    def SetTestResult(self, Result: bool):
        with self.lock:
            self.TestAllData[self.TestName]['Result'] = Result
        self._save_to_json()

    def _save_to_json(self):
        with self.lock:
            with open(self.report_file, 'w') as json_file:
                json.dump(self.TestAllData, json_file, indent=4)

    @classmethod
    def clear_report_file(cls):
        with cls.lock:
            with open(cls.report_file, 'w') as json_file:
                json_file.write('{}')

    @classmethod
    def clear_report_file(cls):
        with cls.lock:
            with open(cls.report_file, 'w') as json_file:
                json_file.write('{}')

    @classmethod
    def SetTestCaseNameClassMethod(cls, TestName):
        with cls.lock:
            cls.TestName = TestName
            cls.TestAllData[TestName] = {'log': [],
                                         'StartTime': datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p"),
                                         'EndTime': datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p"),
                                         'Result': False}
        cls._save_to_json_class_method()

    @classmethod
    def SetTestCaseLogClassMethod(cls, LogType, LogMessage):
        log_entry = [datetime.datetime.now().strftime("%I:%M:%S %p"), LogType, LogMessage]
        with cls.lock:
            cls.TestAllData[cls.TestName]['log'].append(log_entry)
            cls.TestAllData[cls.TestName]['EndTime'] = datetime.datetime.now().strftime("%m.%d.%Y %I:%M:%S %p")
        cls._save_to_json_class_method()

    @classmethod
    def SetTestResultClassMethod(cls, Result: bool):
        with cls.lock:
            cls.TestAllData[cls.TestName]['Result'] = Result
        cls._save_to_json_class_method()

    @classmethod
    def _save_to_json_class_method(cls):
        with cls.lock:
            with open(cls.report_file, 'w') as json_file:
                json.dump(cls.TestAllData, json_file, indent=4)


a=ReportData()
# a.clear_report_file()
a.SetTestCaseName('test 1')
a.SetTestCaseLog('info','info first')
a.SetTestCaseLog('info2','info first2')

b=ReportData()

b.SetTestCaseName('test 2')
b.SetTestCaseLog('info','info first')
b.SetTestCaseLog('info2','info first2')
b.SetTestResult(True)