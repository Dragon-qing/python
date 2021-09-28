f = open("test.txt", "r")
str1 = f.read(5)
print(str1)
f.close()

f = open("test.txt", "r")
content = f.readlines()
print(content)
f.close()

f = open("test.txt", "r")
content = f.readline()
print(content)
content = f.readline()
print(content, type(content))
f.close()

f = open("test.txt", "a+")
f.seek(0, 0)
content = f.read()
print(content)
f.close()

