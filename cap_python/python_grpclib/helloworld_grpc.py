# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: helloworld.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import helloworld_pb2


class GreeterBase(abc.ABC):

    @abc.abstractmethod
    async def SayHello(self, stream: 'grpclib.server.Stream[helloworld_pb2.HelloRequest, helloworld_pb2.HelloReply]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/helloworld.Greeter/SayHello': grpclib.const.Handler(
                self.SayHello,
                grpclib.const.Cardinality.UNARY_UNARY,
                helloworld_pb2.HelloRequest,
                helloworld_pb2.HelloReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SayHello = grpclib.client.UnaryUnaryMethod(
            channel,
            '/helloworld.Greeter/SayHello',
            helloworld_pb2.HelloRequest,
            helloworld_pb2.HelloReply,
        )