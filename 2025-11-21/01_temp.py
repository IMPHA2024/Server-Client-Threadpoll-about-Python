import requests

# 1. 定义请求的 URL
url = 'https://jsonplaceholder.typicode.com/posts'

# 2. 定义要发送的 JSON 数据 (对应 Postman 的 Body)
payload = {
    "title": "foo",
    "body": "bar",
    "userId": None
}

# 3. 发送 POST 请求
# 使用 json=payload 参数，requests 会自动设置 Content-Type 为 application/json
response = requests.post(url, json=payload)

# 4. 处理响应
print("状态码:", response.status_code)
print("响应体:", response.json())