import requests
import os
import selenium
#
#
# # ad=requests.get("https://hospitalb.com")
# # print(ad.text)
# import re
# import requests
#
# # Send a GET request to the URL
# url = 'https://hospitalb.com'
#
# response = requests.get(url)
# # print(response.text)
# print(response.headers)
# response_headers=response.headers
#
#
#
# # Print the tokens
#
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Use regular expressions to find the value of the _token input field
#     match = re.search(r'<input type="hidden" name="_token" value="([^"]+)"', response.text)
#     xsrf_token_match = re.search(r'XSRF-TOKEN=([^;]+)', response_headers['Set-Cookie'])
#     hospital_b_session_match = re.search(r'hospital_b_session=([^;]+)', response_headers['Set-Cookie'])
#     if match:
#         token_value = match.group(1)
#         xsrf_token = xsrf_token_match.group(1)
#         hospital_b_sessiond = hospital_b_session_match.group(1)
#         print("Token value:", token_value)
#         print("XSRF Token:", xsrf_token)
#         print("Hospital B Session:", hospital_b_sessiond)
#     else:
#         print("Token not found in the HTML response.")
# else:
#     print("Failed to fetch the page. Status code:", response.status_code)
# dataidpasst=dict(_token=token_value,
#                 email= 'admin%40gmail.com',
#                 password = '123456')
# headerdata= {'XSRF-TOKEN':xsrf_token,"hospital_b_session":hospital_b_sessiond}
# re=requests.post('https://hospitalb.com/login',data=dataidpasst,headers=headerdata)
# print(re.cookies)
#
# print(re.text)
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
#
# from utilities import readExcel
# path='C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx'
# a=readExcel.getColumnCount('C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx','LDS')
# print(a)
# b=readExcel.getRowCount('C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx','LDS')
# print(b)
# d=readExcel.readData('C:\\Users\\ADMIN\\Desktop\\AkashAutomationDemoProject\\TestData\\Logindata.xlsx','LDS',6,1)
# print(d)
# # def alldata(path1,sheetName):
# #     data=[]
# #     for r in range (2,readExcel.getRowCount(path1,sheetName)):
# #
# #         data2=[]
# #         data2.append(readExcel.readData(path1,sheetName,r,1))
# #         data2.append(readExcel.readData(path1,sheetName,r,2))
# #         data.append(data2)
# #         data2=[]
# #     return data
# print(readExcel.alldata(path,'LDS'))

# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
#
# driver.get('https://hospitalb.com/login')
#
# driver.find_element('xpath',"//input[@name='email']").send_keys('admin@gmail.com')
# driver.find_element('xpath',"//input[@name='password']").send_keys('123456')
# driver.find_element('xpath',"//input[@type='submit']").click()
# time.sleep(2)
# driver.find_element('xpath',"//span[normalize-space()='Admin']").click()
# driver.find_element('xpath',"//a[normalize-space()='Sign out']").click()
# time.sleep(2)
# driver.close()
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

# Define the Selenium test case
# @pytest.mark.selenium
# def test_google_search():
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome()
#
#     # Open Google and log in Extent Report
#     subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Open Google", "INFO"])
#     driver.get("https://www.google.com")
#
#     # Find the search box and enter "akash" and log in Extent Report
#     subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Search for 'akash' on Google", "INFO"])
#     search_box = driver.find_element(By.NAME,"q")
#     search_box.send_keys("akash")
#     search_box.send_keys(Keys.RETURN)
#
#     # Find the search results and click on the "Akash - Wikipedia" link and log in Extent Report
#     subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Click on 'Akash - Wikipedia' link", "INFO"])
#     driver.find_element(By.PARTIAL_LINK_TEXT,"Akash - Wikipedia").click()
#
#     # Extract the page title and log in Extent Report
#     subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Extract page title", "INFO"])
#     page_title = driver.title
#
#     # Close the browser
#     subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Close browser", "INFO"])
#     driver.quit()
#
#     # Assert that the page title contains "Akash" and log in Extent Report
#     if "Akash" in page_title:
#         subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Page title contains 'Akash'", "PASS"])
#     else:
#         subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "logStep", "Page title does not contain 'Akash'", "FAIL"])
#
# # Execute Java code to close Extent Report
# subprocess.run(["java", "-cp", "extentreport.jar", "com.example.ExtentReportGenerator", "closeReport"])
#

#
# Screenshots Funcation
screenshot_folder = 'Screenshot'
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenshot_path = os.path.join(current_directory, screenshot_folder)
print(screenshot_path)

# driver = webdriver.Chrome()
# driver.get('https://hospitalb.com/login')
# driver.get_screenshot_as_file(screenshot_path+r'\Akash.png')
from utilities.browser import browserindex
a= 'akash-dilwaletest'
if a.count('-')==0:
    print('- not')
    print(a)
elif a.count('-')==1:
    print('count 1')
    print(a.split("-")[0])
elif a.count('-')==2:
    print('count 2')
    print('-'.join(a.split("-")[0:-1]))

print("-----------------------------------------")
print(a.count('-'))
print((a.split('-')[0:browserindex()]))
new_a = '-'.join(a.split('-')[0:browserindex()])

print(new_a)
# if a.count('-')==1:
#     a=a.split('-')[0:-1]
#     print(a)
#     a="".join(a)
#     print(a)
# if a.count('-')==2:
#     a=a.split('-')[0:-1]
#     print(a)
#     a="".join(a)
#     print(a)
# a=a.replace('a','-').replace('b','-')
# print(a)