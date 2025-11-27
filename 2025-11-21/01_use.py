import requests

url ="https://uapis.cn/api/v1/misc/weather"


locat = {
    "city" : "浦东",
    "adcode" : "201306"
}
response = requests.get(url,params=locat)
data = response.json()

print(response)
print(data)