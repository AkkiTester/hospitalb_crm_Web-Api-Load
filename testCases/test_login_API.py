import pytest
import requests
from utilities.readconfig import Readconfig
from utilities.customLogger import LogGen


# pytest.mark.skip('Api')
# def test_Check_Login_Api():
#     headers = {
#         'authority': 'hospitalb.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'en-US,en;q=0.9',
#         'cache-control': 'max-age=0',
#         'cookie': 'XSRF-TOKEN=eyJpdiI6Im02aFlSc0RKQTZLSXY0ZDVpQnNzcEE9PSIsInZhbHVlIjoiT0tEV01DTFArZDBaXC9qNXdWZk4yYWh1M3ZnUlJheHNqYURVN05Ld1pNaHFCK0RRZmQ5b3h1VysrK2t1WE1ZQ2lRZUt4Y0VaaWFaRVBxNmhqeDBQdk9aTStrbjVHSlVGbHNFb0pHUWNJazlFdU1YRHpWdzQrMXBuWnRybVwvWEZ5ayIsIm1hYyI6ImY2NDg1MGFlMzUwNmQ3MWJmYzBlNDExYmRmYjRhYzhjODA3ZjZkMjNjMmE4N2U2MjM1ZmZhOWUxMjAyOTIzMzAifQ%3D%3D; hospital_b_session=eyJpdiI6IjdSSW1pU1YyVXFsV1ZxWGo0YjF4akE9PSIsInZhbHVlIjoiSGNkZ2pSbE1hK210bE5DNmVLcktpcWx3UEgrUFhQS25LXC9LcmZjblwvaEEwS1JPb2lOK3dqRG9vTGNUQU0rOWlWNjJhNUgrRFJhQ0tERkFnT1p0YlBvMDh2bTVKckViek9GVG8rQlFzeWtZdUtlU2V0MHV3cUJreklLcjJ0THFYZyIsIm1hYyI6Ijc2NTM0YTM5OWI2MDI4MGRjNWYzZWQ4NTgyOTJmMjQ0NDZjMjJjNmE4YzFkODRkNDdlYzFmYzZiMjI1ZDc0YTgifQ%3D%3D',
#         'referer': 'https://hospitalb.com/login',
#         'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#         'sec-ch-ua-mobile': '?1',
#         'sec-ch-ua-platform': '"Android"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
#     }
#     LogGen.loggen().info("************Test_Check login start***********")
#     response = requests.get('https://hospitalb.com/', headers=headers)
#
#     if 'Admin' in response.text:
#         LogGen.loggen().info("************Test_ Check login Passed***********")
#         assert True
#     else:
#         LogGen.loggen().info("************Test_ Check login Fail***********")
#         assert False
#
#
#
#
#
