a = lambda: 100
print(a())

fn1 = lambda a, b: a+b

print(fn1(1, 2))

fn2 = lambda *args: args
print(fn2(10, 20, 30))

fn3 = lambda **kwargs: kwargs
print(fn3(name="python", age=20))

names = ["jack", "mom", "lily", "Rose", "momm"]
names.sort()
print(names)