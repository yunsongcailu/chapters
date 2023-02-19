# 单python项目推荐 支持语言不多(python,nodejs) msgpack.org 序列化 zeroMQ通信
# 生态不如 grpc 语言支持不如 grpc
# msgpack-python, pyzmq, future, greenlet, gevent
# https://msgpack.org/  ,  https://github.com/0rpc/zerorpc-python
# https://zerorpc.io

# 一元调用
import zerorpc


class HelloZeroRPC(object):
    def hello(self, name):
        return "Hello, %s" % name


s = zerorpc.Server(HelloZeroRPC())
s.bind("tcp://0.0.0.0:4242")
print("RPC_ZERORPC_SERVER Listen on TCP 4242")
s.run()

# 流式调用
