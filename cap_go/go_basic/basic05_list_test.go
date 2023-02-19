package go_basic

import (
	"fmt"
	"testing"
)

func TestBasicList(t *testing.T) {
	// go中的数组长度固定,切片和python中的list更接近
	var courses [5]string
	hobbies := [3]string{"music", "movie", "computer"}
	friends := [...]float64{1.1, 2.2, 3.3}
	courses[0] = "golang"
	hobbies[2] = "python"
	fmt.Println(courses[0], hobbies, friends)
	for i := 0; i < len(friends); i++ {
		fmt.Println(friends[i])
	}
	for i, friend := range friends {
		fmt.Printf("index:%d,value:%f", i, friend)
	}
	book1 := []string{"aaa", "bbb"}
	book2 := make([]string, 5)
	var book3 []string
	fmt.Println(book1, book2, book3)
}
