package go_basic

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

func TestJudgment(t *testing.T) {
	num := 12
	if num%2 == 0 {
		println("偶数")
	} else {
		println("奇数")
	}
	for index, value := range []rune("云松采露") {
		fmt.Printf("%d,%c\n", index, value)
	}
	rand.Seed(time.Now().UnixNano())
	getScore := func() {
		score := rand.Int31n(100)
		switch {
		case score > 90 && score <= 100:
			fmt.Println(score, "A")
		case score > 80 && score <= 90:
			fmt.Println(score, "B")
		case score > 70 && score <= 80:
			fmt.Println(score, "C")
		case score > 60 && score <= 70:
			fmt.Println(score, "D")
		case score > 50 && score <= 60:
			fallthrough
		case score > 40 && score <= 50:
			fmt.Println(score, "E")
		default:
			fmt.Println(score, "-")
		}
	}
	for i := 0; i < 20; i++ {
		getScore()
	}
}
