import jsonrpclib

server = jsonrpclib.ServerProxy("http://192.168.1.136:8080")
print(server.add(2, 3))
