def judgment():
    num = 12
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
    i = 1
    while i <= 10:
        print(i)
        i = i + 1
    for i in range(1,11):
        print(i)
    print(sum(range(1,11)))
    for index,value in enumerate("yunsongcailu"):
        print(index,value)
    print("python 中没有switch 可以使用list实现,key做条件,value调用处理函数")


if __name__ == "__main__":
    judgment()
