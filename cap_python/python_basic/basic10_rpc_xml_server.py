# 了解
from xmlrpc.server import SimpleXMLRPCServer


class Cal:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def subtract(x, y):
        return abs(x - y)

    @staticmethod
    def divide(x, y):
        return x / y


obj = Cal()
server = SimpleXMLRPCServer(("", 8088))
# 注册实例
server.register_instance(obj)
print("RPC_XML_SERVER Listen on 8088")
server.serve_forever()
