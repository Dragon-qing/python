str1 = "a"
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
tuple1 = ("go ",)
print(str1 * 4)
print(list1 * 5)
print(tuple1 * 6)

for i in range(1, 10, 1):
    print(i, end="")
for i in enumerate(list1, start=1):
    print(i)