package go_basic

import (
	"fmt"
	"testing"
)

const Author = "yun song"
const (
	UnKnown = 0
	Female  = 1
	Male    = 2
)

var langCount int = 2
var firstLang, secondLang string

func TestHelloWord(t *testing.T) {
	fmt.Println("hello world")
	firstLang, secondLang = "golang", "python"
	fmt.Printf("Learn %s at the same time as learning %s,count:%d\n", firstLang, secondLang, langCount)
	// 定义局部变量
	var i int = 10
	j := i - 1
	for k := 0; k <= i; k++ {
		if i > 20 {
			break
		}
		fmt.Printf("i:%d,j:%d,k:%d\n", i, j, k)
		i++
	}
	myList := []string{"tom", "lili", "andy"}
	for index, item := range myList {
		fmt.Printf("index:%d,value:%s\n", index, item)
	}
	// 匿名变量
	for _, item := range myList {
		fmt.Printf("value:%s\n", item)
	}
	// 常量
	fmt.Printf("go 中常量定义 不能在语法层面修改,python并没有常量的定义,作者:%s\n", Author)
	fmt.Println("python中可以使用元组定义为不可修改的常量")
	fmt.Printf("%d,%d,%d\n", UnKnown, Female, Male)
}
