# pip install requests -i https://pypi.douban.com/simple
import requests

response = requests.get("http://127.0.0.1:8003/?name=tom&age=18")
print(response.text)
