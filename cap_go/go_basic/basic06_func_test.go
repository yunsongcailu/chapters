package go_basic

import (
	"fmt"
	"io"
	"os"
	"testing"
)

func TestBasicFunc(t *testing.T) {
	var add func(a, b int) int
	add = func(a, b int) int {
		return a + b
	}
	fmt.Println(add(1, 2))
	f, _ := os.Open("demo.txt")
	x := 10
	defer func(a int) {
		fmt.Println("x:", a)
		f.Close()
	}(x)
	defer func() {
		fmt.Println("x2:", x)
	}()
	x += 1
	text, err := io.ReadAll(f)
	if err != nil {
		t.Fatal(err)
	}
	t.Log(text)
}
