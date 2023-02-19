from inspect import getfullargspec
from typing import get_type_hints
from functools import wraps


def data_types():
    pass_exam = False
    print(f'是否通过考试:{pass_exam}')
    age = 18
    import sys
    print(f'int类型占用动态字节,例如18占用:%d,不用担心超出上限\n' % sys.getsizeof(age))
    print(type(age), age)
    str_age = str(age)
    print(type(str_age), str_age)
    int_age = int(age)
    print(type(int_age), int_age)
    score = "99.99"
    float_score = float(score)
    print(type(float_score), float_score)
    print(type(str(float_score)), str(float_score))
    print("非空字符串转布尔均为true", bool("aaa"), "严格模式使用from distutils.util import strtobool")
    from distutils.util import strtobool
    print(strtobool("False"))
    print("python 海象运算符 := 为表达式赋值,跟 go 的 := 赋值不同")
    course_list = ["django", "scrapy", "tornado"]
    if len(course_list) >= 3:
        print("数量: {}".format(len(course_list)))
    # 重复计算len() 使用 海象运算符解决
    if (list_size := len(course_list)) >= 3:
        print("数量: {}".format(list_size))
    print("python一般使用变量名隐士说明数据类型,更好的办法是声明变量类型,仅仅做为 关键变量 提示的作用并不影响实际类型")
    my_age: int = 18
    my_name: str = "yun song"
    my_gender: bool = True
    my_height: float = 165.2
    my_x: bytes = b"byte"
    from typing import List, Set, Dict, Tuple
    course: List[str] = ["django", "scrapy", "tornado"]
    print(type(my_age), my_age, type(my_name), my_name, type(my_x), my_x, type(course), course)
    print("获取函数形参定义时的数据类型")
    print(add.__annotations__)
    add("1", 2.0)


def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)
    for item_name, item_type in hints.items():
        if item_name == "return":
            continue
        if not isinstance(kwargs[item_name], item_type):
            raise TypeError("参数: {} 类型错误, 应该是: {}".format(item_name, item_type))


# 使用装饰器
def type_validater(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        validate_input(decorator, **kwargs)
        return decorator

    return wrapped_decorator


@type_validater
def add(a: int, b: float) -> float:
    # validate_input(add, a=a, b=b)
    return a + b


if __name__ == "__main__":
    data_types()
