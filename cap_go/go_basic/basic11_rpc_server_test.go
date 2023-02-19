package go_basic

import (
	"fmt"
	"net"
	"net/rpc"
	"testing"
)

type HelloRpc struct{}

func (hr *HelloRpc) Hello(name string, reply *string) error {
	*reply = "hello" + name
	return nil
}

func TestRpcServer(t *testing.T) {
	listener, err := net.Listen("tcp", ":4242")
	if err != nil {
		fmt.Println(err)
		return
	}
	if err = rpc.RegisterName("HelloService", &HelloRpc{}); err != nil {
		fmt.Println(err)
		return
	}
	conn, err := listener.Accept()
	if err != nil {
		panic(err)
	}
	fmt.Println("RPC server listen on 4242")
	rpc.ServeConn(conn)
}
