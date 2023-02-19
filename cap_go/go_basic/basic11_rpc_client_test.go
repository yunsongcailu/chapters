package go_basic

import (
	"net/rpc"
	"testing"
)

func TestRpcClient(t *testing.T) {
	client, err := rpc.Dial("tcp", ":4242")
	if err != nil {
		panic(err)
	}
	var result string
	err = client.Call("HelloRpc.Hello", "anan", &result)
	if err != nil {
		panic(err)
	}
	t.Log(result)
}
