from typing import List
from copy import deepcopy

courses = []
hobbies = list(["music", "movie", "computer"])
for item in hobbies:
    print(item)

print("python中是引用传递,使用deepcopy可以实现数据隔离,golang中是值传递")


def print_hobbies(hobbies: List[str]):
    hobbies[0] = "python"
    print(hobbies)


print_hobbies(deepcopy(hobbies))
print(hobbies)
a = None
b = None
print("python None 是全局变量 不等于go nil",id(a),id(b))