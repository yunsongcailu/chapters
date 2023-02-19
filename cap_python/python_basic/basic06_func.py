def add(a, b):
    return a + b


def read_file(filename):
    with open(filename) as f:
        sum = 0
        for line in f:
            sum += int(line)
    return sum


if __name__ == "__main__":
    print(add(2, 2))
    print(read_file("demo.txt"))
