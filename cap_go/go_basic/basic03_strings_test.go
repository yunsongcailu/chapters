package go_basic

import (
	"fmt"
	"strings"
	"testing"
)

func TestBasicStrings(t *testing.T) {
	name := "昵称:\"云松\""
	name = `昵称:"云松"`
	runeName := []rune(name)
	fmt.Printf("name:%s, len:%d,go 一中文三个字节\n,runeName len:%d 长度和python的长度一致\n转义字符占一个字节\n", name, len(name), len(runeName))
	fmt.Printf("是否包含子串:%v\n,位置:%d,出现次数:%d,前缀:%v,后缀:%v\n",
		strings.Contains(name, "云松"),
		strings.Index(name, "云松"),
		strings.Count(name, "云松"),
		strings.HasPrefix(name, "昵"),
		strings.HasSuffix(name, "\""))
	blogURL := " www.Blog_URL.com "
	fmt.Printf("toUpper:%s,toLower:%s\n", strings.ToUpper(blogURL), strings.ToLower(blogURL))
	fmt.Printf("字符串比较ASCII码:%v,%v\n", strings.Compare(name, blogURL), strings.Compare(blogURL, name))
	fmt.Printf("去掉前后空格:%s,按字符去掉前后:%s,分割:%v,合并:%s\n替换:%s",
		strings.TrimSpace(blogURL),
		strings.Trim(blogURL, " "),
		strings.Split(blogURL, "."),
		strings.Join([]string{"www", "blog", "url", "com"}, "."),
		strings.Replace(blogURL, "_", "-", -1))

}
