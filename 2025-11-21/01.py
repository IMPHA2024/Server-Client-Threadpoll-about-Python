import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "http://uat.jhj.com.cn/test-api/ocean-business-inner/shase/logisticsOperator/search"

response = requests.get(url)

'''
print(response.status_code)
print(response.headers)
print(response.text)
'''
data=response.json()

print(data)