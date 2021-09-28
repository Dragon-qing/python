def sum_num(a, b, c):
    return a + b + c


def avg_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


print(type(avg_num(2, 2, 3)), avg_num(2, 2, 3))
