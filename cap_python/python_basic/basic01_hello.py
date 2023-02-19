def hello():
    print('hello world')
    lang_count = 2
    first_lang, second_lang = "go", "python"
    print(f'Learn %s at the same time as learning %s,count:%d\n' % (first_lang, second_lang, lang_count))
    i = 10
    j = i - 1
    k = 0
    while k <= i:
        if i >= 20:
            break
        print(f'i:%d,j:%d,k:%d\n' % (i, j, k))
        i = i + 1
        k = k + 1


if __name__ == "__main__":
    hello()
    # 匿名变量
    my_list = ["tom", "lili", "andy"]
    for item in my_list:
        print(item)
    for index, item in enumerate(my_list):
        print(f'index:%d,value:%s\n' % (index, item))
        # 匿名变量
    for index, item in enumerate(my_list):
        print(f'value:%s\n' % item)
    # 常量
    AUTHOR = "yun song"
    print("python 并没有强制常量设计,作者:", AUTHOR)
    print("python中可以使用元组来定义为不可修改的常量")
    sex_tuple = ("unknown", "male", "female")
    print(sex_tuple[0], sex_tuple[1], sex_tuple[2],)
