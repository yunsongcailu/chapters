import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl

host = ('', 8003)


# RPC 就是将URL 映射到需要调用的函数
class AddHandler(BaseHTTPRequestHandler):
    # GET 必须大写
    def do_GET(self):
        # 解析请求地址
        parsed_url = urlparse(self.path)
        print(self.path)
        # 提取GET请求参数
        qs = dict(parse_qsl(parsed_url.query))
        name = qs.get("name", "")
        age = qs.get("age", "")
        # 业务逻辑省略
        result = {
            "name": name,
            "age": age
        }
        self.send_response(200, "OK")
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(host, AddHandler)
    print("server running on 8003")
    server.serve_forever()
