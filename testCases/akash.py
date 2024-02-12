import requests


# ad=requests.get("https://hospitalb.com")
# print(ad.text)
import re
import requests

# Send a GET request to the URL
url = 'https://hospitalb.com'

response = requests.get(url)
# print(response.text)
print(response.headers)
response_headers=response.headers



# Print the tokens

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Use regular expressions to find the value of the _token input field
    match = re.search(r'<input type="hidden" name="_token" value="([^"]+)"', response.text)
    xsrf_token_match = re.search(r'XSRF-TOKEN=([^;]+)', response_headers['Set-Cookie'])
    hospital_b_session_match = re.search(r'hospital_b_session=([^;]+)', response_headers['Set-Cookie'])
    if match:
        token_value = match.group(1)
        xsrf_token = xsrf_token_match.group(1)
        hospital_b_sessiond = hospital_b_session_match.group(1)
        print("Token value:", token_value)
        print("XSRF Token:", xsrf_token)
        print("Hospital B Session:", hospital_b_sessiond)
    else:
        print("Token not found in the HTML response.")
else:
    print("Failed to fetch the page. Status code:", response.status_code)
dataidpasst=dict(_token=token_value,
                email= 'admin%40gmail.com',
                password = '123456')
headerdata= {'XSRF-TOKEN':xsrf_token,"hospital_b_session":hospital_b_sessiond}
re=requests.post('https://hospitalb.com/login',data=dataidpasst,headers=headerdata)
print(re.cookies)

print(re.text)
