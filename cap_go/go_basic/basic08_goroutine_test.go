package go_basic

import (
	"fmt"
	"testing"
	"time"
)

func TestBasicGoroutine(t *testing.T) {
	// deadline
	// 1. 如果没有缓冲,在没有消费者时生产数据
	// 2. 生产数据结束要关闭

	ch1, ch2, ch3 := make(chan int), make(chan int), make(chan int)
	//var wg sync.WaitGroup

	go func(ch chan int) {
		//wg.Add(1)
		for {
			time.Sleep(time.Second)
			fmt.Println("send 1 to ch1")
			ch <- 1
		}
	}(ch1)
	go func(ch chan int) {
		//wg.Add(1)
		for {
			time.Sleep(time.Second)
			fmt.Println("send 2 to ch2")
			ch <- 2
		}
	}(ch2)

	go func(ch chan int) {
		time.Sleep(time.Second * 10)
		ch3 <- 3
	}(ch3)

	count, data := 0, 0
	for {
		if count >= 10 {
			break
		}
		select {
		case x := <-ch1:
			data = x
		case x := <-ch2:
			data = x
		}
		count++
		fmt.Println("data:", data)
	}
	select {
	case <-ch3:
		fmt.Println("ch3  timeout ... break")
	}
	fmt.Println("return")
}
