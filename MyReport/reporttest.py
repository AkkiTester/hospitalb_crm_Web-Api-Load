from My_Report_Data_Main import ReportData
a=ReportData()
a.SetTestCaseName('TestName3')
a.SetTestCaseLog('LogType1','LogMassage1')
a.SetTestResult(True)

ReportData.SetTestCaseNameClassMethod('test 3')
ReportData.SetTestCaseLogClassMethod('info', 'info first')
ReportData.SetTestCaseLogClassMethod('info2', 'info first2')
ReportData.SetTestResultClassMethod(True)