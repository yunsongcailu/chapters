from xmlrpc import client

server = client.ServerProxy("http://192.168.1.136:8088")
print(server.add(5, 6))
print(server.multiply(5, 6))
