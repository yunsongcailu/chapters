# rpc client demo
import json

import requests


class RpcClient:
    def __init__(self, url):
        self.url = url

    def request_get_demo(self, name, age):
        response = requests.get(f'%s/?name=%s&age=%s' % (self.url, name, age))
        print(response.text)
        return json.loads(response.text).get("result", 0)


client = RpcClient("http://192.168.1.136:8003")
client.request_get_demo("tom", 19)
