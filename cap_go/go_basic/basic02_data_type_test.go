package go_basic

import (
	"fmt"
	"strconv"
	"testing"
	"unsafe"
)

func TestDataTypes(t *testing.T) {
	// 定义布尔类型
	passExam := false
	fmt.Printf("是否通过考试:%v\n", passExam)
	// 整数类型
	fmt.Println("int是动态类型,受机器或系统位数影响,一般会指定大小使用.python中是动态分配,不用担心超出上限.")
	var age uint8 = 127
	var score int = 127
	fmt.Printf("年龄uint8大小:%d,占用字节:%d\n分数int大小:%d,占用字节:%d\n", age, unsafe.Sizeof(age), score, unsafe.Sizeof(score))
	// 浮点型
	height := 178.2
	fmt.Printf("浮点型默认跟随系统位:%T\n", height)
	// byte类型
	fmt.Println("byte类型是uint8的别名,rune是int32的别名")
	var aByte byte = 'a'
	var aRune rune = 'a'
	fmt.Printf("abyte:%v,%T\n aRune:%v,%T\n aRune+1:%c,%T\n", aByte, aByte, aRune, aRune, aRune+1, aRune+1)
	intHeight := int(height)
	fmt.Printf("强转类型float64:%f, int(float64):%d,强转回来:%f\n", height, intHeight, float64(intHeight))
	stringHeight := strconv.FormatFloat(height, 'f', -1, 64)
	stringToHeight, _ := strconv.ParseFloat(stringHeight, 64)
	fmt.Printf("float64:%f,转为string:%s,再转回来:%f\n", height, stringHeight, stringToHeight)
	stringIntHeight := strconv.Itoa(intHeight)
	stringToIntHeight, _ := strconv.Atoi(stringIntHeight)
	fmt.Printf("int:%d,转为string:%s,再转回来:%d\n", intHeight, stringIntHeight, stringToIntHeight)
	// 指定不同进制转换
	stringTo16int, _ := strconv.ParseInt(stringIntHeight, 16, 64)
	fmt.Printf("指定进制 ParseInt:%v\n", stringTo16int)

}
