from concurrent import futures

import grpc

import demo_pb2
import demo_pb2_grpc


class Greeter(demo_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return demo_pb2.HelloReply(message=f"你好,{request.name},这里是python 50051")


if __name__ == "__main__":
    # 实例化server 一定要小写server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on 50051")
    server.wait_for_termination()

'''
from logging import basicConfig, getLogger, INFO

import grpc
import threading
import signal
from concurrent import futures

from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

import {your proto}_pb2
import {your proto}_grpc


logger = getLogger(__name__)


def serve():
    # Set up server
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=100))

    # Generate servicer's implementation
    {your servicer} = {your servicer}Impl()
    health_servicer = health.HealthServicer(
            experimental_non_blocking=True,
            experimental_thread_pool=
                futures.ThreadPoolExecutor(max_workers=100))

    # Register servicers
    logger.info('register HealthServicer to server')
    health_pb2_grpc.add_HealthServicer_to_server(
        health_servicer, server)
    logger.info('register your servicer to server')
    {}_grpc.add_{}_to_server({}, server)

    # Find services
    services = tuple(
        service.full_name for service
            in {}.DESCRIPTOR.services_by_name.values()) + (
                reflection.SERVICE_NAME, health.SERVICE_NAME)
    logger.info('Registered Services: {}'.format(services))

    # Mark all services as healthy.
    for service in services:
        logger.info('servicer: {}, set status: SERVING'.format(service))
        health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)

    # Enable reflection
    reflection.enable_server_reflection(services, server)

    # Start gRPC server
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info('Start gRPC server with port: 50051')

    # wait until got SIGTERM, and will exec graceful shut down.
    done = threading.Event()
    def on_done(signum, frame):
        logger.info('Got signal {}, {}'.format(signum, frame))
        done.set()
    signal.signal(signal.SIGTERM, on_done)
    done.wait()

    logger.info('Waiting for RPCs to complete...')
    # Mark all services as NOT_SERVING.
    health_servicer.enter_graceful_shutdown()
    server.wait_for_termination(10)

    # Stop server
    server.stop(10)
    logger.info('Stoped gRPC server')


if __name__ == '__main__':
    basicConfig()
    serve()
'''
