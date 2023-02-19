# 了解 基于json的rpc库有两个: jsonrpc 和 jsonrpclib
# workon django2_2023
# pip install jsonrpclib-pelix -i https://pypi.douban.com/simple
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from jsonrpclib.threadpool import ThreadPool

# Setup the thread pool: between 0 and 10 threads
pool = ThreadPool(max_threads=10, min_threads=0)

# Don't forget to start it
pool.start()

# Setup the server
server = SimpleJSONRPCServer(('', 8080))
server.set_notification_pool(pool)

# Register methods
server.register_function(pow)
server.register_function(lambda x, y: x + y, 'add')
server.register_function(lambda x: x, 'ping')

try:
    print("RPC_JSON_SERVER Listen on 8080")
    server.serve_forever()
finally:
    # Stop the thread pool (let threads finish their current task)
    pool.stop()
    server.set_notification_pool(None)
