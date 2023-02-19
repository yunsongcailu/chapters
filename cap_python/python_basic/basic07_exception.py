# 错误和异常
def div(a, b):
    if b == 0:
        # 方式1:返回异常 raise Exception("b == 0")
        # 方式2:返回错误
        return None, "被除数不能为0"
    return a / b, None


if __name__ == "__main__":
    # try:
    #     div(2, 0)
    # except Exception as e:
    #     print(e)
    res, err = div(2, 0)
    if err is not None:
        print(err)
    else:
        print(res)
