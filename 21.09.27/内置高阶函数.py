import functools
list1 = [1, 2, 3, 4, 5]


def method(x):
    return x+1


def method1(x, y):
    return x + y


def method2(x):
    return x % 2 == 0


result = map(method, list1)
print(result)
print(tuple(result))
print("="*20)

result = functools.reduce(method1, list1)
print(result)
result = filter(method2, list1)
print(result)
print(list(result)) 