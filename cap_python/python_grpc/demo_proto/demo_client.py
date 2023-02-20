import grpc
import demo_pb2
import demo_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel("0.0.0.0:50051") as channel:
        stub = demo_pb2_grpc.GreeterStub(channel)
        resp: demo_pb2.HelloReply = stub.SayHello(demo_pb2.HelloRequest(name="tom"))
        print(resp.message)

    with grpc.insecure_channel("0.0.0.0:5051") as go_channel:
        stub = demo_pb2_grpc.GreeterStub(go_channel)
        resp: demo_pb2.HelloReply = stub.SayHello(demo_pb2.HelloRequest(name="lili"))
        print(resp.message)
