from threading import Lock  # Import Lock for thread safety (optional)
class ReportData:
    TestAllData = {}  # Now an instance-specific dictionary
    def __init__(self):
        self.TestName = ''
        self.TestLog = []
        self.TestResult = False
        # self.TestAllData = {}  # Now an instance-specific dictionary

        # Optional: Use a lock for thread safety if required
        self.data_lock = Lock()

    def SetTestCaseName(self, TestName):
        self.TestName = TestName
        self.TestAllData[TestName] = []
        self.TestAllData[TestName + 'Result'] = []

    def SetTestCaseLog(self, LogType, LogMessage):
        # Acquire the lock if using threading (optional)
        if hasattr(self, 'data_lock'):
            with self.data_lock:
                self.TestAllData[self.TestName].append((LogType, LogMessage))
                self.TestLog.append((LogType, LogMessage))
        else:
            self.TestAllData[self.TestName].append((LogType, LogMessage))
            self.TestLog.append((LogType, LogMessage))

    def SetTestResult(self, Result: bool):
        # Acquire the lock if using threading (optional)
        if hasattr(self, 'data_lock'):
            with self.data_lock:
                self.TestAllData[self.TestName + 'Result'].append(Result)
                self.TestResult = Result
        else:
            self.TestAllData[self.TestName + 'Result'].append(Result)
            self.TestResult = Result

    def GetTestAllData(self):
        # Return a copy to avoid modification of original data
        return self.TestAllData.copy()

# Create instances of ReportData
report_data1 = ReportData()
report_data2 = ReportData()

# Set test case name and log for report_data1
report_data1.SetTestCaseName(TestName='My test 1')
report_data1.SetTestCaseLog(LogType='Info', LogMessage='akashLog 1')
report_data1.SetTestCaseLog(LogType='Info', LogMessage='akashLog 2')
report_data1.SetTestResult(Result=True)

# Set test case name and log for report_data2 (independent data)
report_data2.SetTestCaseName(TestName='My test 2')
report_data2.SetTestCaseLog(LogType='Info', LogMessage='Another test log')
report_data2.SetTestCaseLog(LogType='Info', LogMessage='Another test log')
report_data2.SetTestResult(Result=False)

# Get and print TestAllData for each instance (independent data)
print(report_data1.GetTestAllData())  # Output: {'My test 1': [('Info', 'akashLog 1'), ('Info', 'akashLog 2')], 'My test 1Result': [True]}
print(report_data2.GetTestAllData())  # Output: {'My test 2': [('Info', 'Another test log')], 'My test 2Result': [False]}
print(ReportData.TestAllData)