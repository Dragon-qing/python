def sum_num(a, b, f):
    return f(a) + f(b)


result = sum_num(1.6, 2, abs)
print(result)