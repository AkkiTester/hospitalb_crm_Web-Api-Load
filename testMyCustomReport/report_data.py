import json
from testMyCustomReport.My_Report_Data_Main import ReportData3
class ReportData:
    TestAllData = {}

    def __init__(self):
        self.ReportName = ''
        self.TestName = ''
        self.TestLog = []
        self.TestResult = False

    def SetReportName(self,Reportname='JsonData'):
        self.ReportName=Reportname
        return Reportname
    def SetTestCaseName(self, TestName):
        self.TestName = TestName
        self.TestAllData[TestName] = []
        # self.TestAllData[TestName + 'Result'] = []

    def SetTestCaseLog(self, LogType, LogMessage):
        self.TestAllData[self.TestName].append((LogType, LogMessage))
        self.TestLog.append((LogType, LogMessage))


    def SetTestResult(self, Result: bool,append_mode=True):
        self.TestAllData[self.TestName + 'Result']=Result
        self.TestResult = Result
        if append_mode:
            # Append data to existing JSON file (if it exists)
            data = {}
            # try:
            #     with open(self.ReportName, 'r') as f:
            #         data = json.load(f)
            # except FileNotFoundError:
            #     pass  # Create a new file if it doesn't exist

            data[self.TestName] = self.TestAllData
            with open(self.ReportName, 'a') as f:
                json.dump(data, f, indent=4)
        else:
            # Overwrite the existing file (if it exists)
            with open(self.ReportName, 'a') as f:
                json.dump(self.TestAllData, f, indent=4)

#
# # Create an instance of ReportData
# report_data = ReportData()
#
# # Set test case name and log
# report_data.SetTestCaseName(TestName='My test')
# report_data.SetTestCaseLog(LogType='Info', LogMessage='akashLog')
# report_data.SetTestCaseLog(LogType='Info', LogMessage='akashLog')
# report_data.SetTestCaseLog(LogType='Info', LogMessage='akashLog')
#
# report_data.SetTestResult(Result=True)
#
# # Access attributes
# print(report_data.TestName)
# print(report_data.TestLog)
# print(report_data.TestResult)
# print(report_data.TestAllData)
#
a=ReportData()
# b=ReportData()
#
a.SetTestCaseName('Test1')
a.SetReportName('akash')
a.SetTestCaseLog('INFO',"Checking Log")
a.SetTestCaseLog('INFO',"Checking Log2")
a.SetTestResult(True)
# print(report_data.TestAllData)
print(ReportData.TestAllData)
a= ReportData3()
a.set_test_case_name('akash')
a.set_test_case_log('Info','Akash')
a.set_test_result(False)