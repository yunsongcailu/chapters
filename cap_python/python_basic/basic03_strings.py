def strings_func():
    name = '昵称:"云松"'
    print(f'name:%s, len:%d,python一中文一个字符,和go 字符串转为[]rune长度一致\n' % (name, len(name)))
    if "云松" in name:
        print("name 包含子串 true")
    print(name.index("云松"), name.count("云松"), name.startswith("昵"), name.endswith("\""))
    blogURL = "www.Blog_URL.com"
    print(f'upper:%s,lower:%s\n' % (blogURL.upper(), blogURL.lower()))
    print("www blog url com".split(" "))
    print(".".join(["www", "blog", "url", "com"]))
    name = input("请输入姓名: ")
    age = int(input('请输入年龄: '))
    print(name,age,type(age))

if __name__ == '__main__':
    strings_func()
