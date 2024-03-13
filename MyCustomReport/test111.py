from MyCustomReport.my import ReportData

c=ReportData()
b=ReportData()

c.SetTestCaseName('Test2')
c.SetTestCaseLog('INFO',"Checking Log")
c.SetTestResult(True)


print(ReportData.TestAllData)