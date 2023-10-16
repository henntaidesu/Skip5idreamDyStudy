import requests
import json
import re

print("欢迎使用盗梦空间抖音学习跳过脚本")

while True:
    userName = input("请输入姓名: ")
    if re.match("^[\u4e00-\u9fa5]+$", userName):
        break
    else:
        print("请输入汉字")

while True:
    studentNo = input("请输入学号: ")
    if re.match("^[a-zA-Z0-9]+$", studentNo):
        break
    else:
        print("学号只能是字母和数字")

schoolName = input("请输入学校名称: ")

# 目标URL
url = "https://h5.5idream.net/training/apply"
# 要传递的数据
data = {
    "userName": userName,
    "studentNo": studentNo,
    "schoolName": schoolName,
    "type": 8
}

# 发送POST请求
response = requests.post(url, data=data)
response_data = json.loads(response.text)

# 检查响应状态码
if response.status_code == 200:
    if "data" in response_data and response_data["data"]:
        print("POST请求成功，成功跳过盗梦空间抖音学习")
    if "data" in response_data and response_data["code"] == "学号只能是字母和数字":
        print("检查学校是否正确")
    else:
        print("检查学校名称是否正确")
else:
    print(f"POST请求失败，状态码: {response.status_code}")

# 可以输出响应内容以查看返回结果

