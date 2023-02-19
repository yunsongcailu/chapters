package go_basic

import (
	"fmt"
	"sync"
	"testing"
)

var max, total = 100000, 0
var wg sync.WaitGroup

// 互斥锁
var lock sync.Mutex

// 读写锁
// var rwLock sync.RWMutex

func add() {
	defer wg.Done()
	for i := 0; i < max; i++ {
		lock.Lock()
		//rwLock.Lock()
		total += 1
		//rwLock.Unlock()
		lock.Unlock()
	}
}

func sub() {
	defer wg.Done()
	for i := 0; i < max; i++ {
		lock.Lock()
		//rwLock.RLock()
		total -= 1
		//rwLock.RUnlock()
		lock.Unlock()
	}
}

func TestBasicMutex(t *testing.T) {
	wg.Add(2)
	go add()
	go sub()
	wg.Wait()
	fmt.Println(total)
}
