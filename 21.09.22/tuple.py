t2 = (10,)
print(type(t2))
t1 = (10, 20, 30, 10)
print(type(t1))

print(t1.index(10))
print(t1.count(10))
print(len(t1))

t3 = ("a", "bb", [123, 23])
print(t3[2])
t3[2][0] = 111
print(t3)
