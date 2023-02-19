package go_basic

import (
	"context"
	"fmt"
	"testing"
	"time"
)

func TestBasicContext(t *testing.T) {
	// withCancel ctx
	ctx1, cancel := context.WithCancel(context.Background())
	go printInfo(ctx1)
	time.Sleep(time.Second * 6)
	cancel()
	time.Sleep(time.Second)
}

func printInfo(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println("printInfo ctx withCancel done")
			return
		default:
			time.Sleep(time.Second)
			fmt.Println("printInfo print...")
		}
	}
}
