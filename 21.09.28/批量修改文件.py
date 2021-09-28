import os
flag = 2
files = os.listdir()
print(files)
for i in files:
    if i.endswith(".py"):
        # 增加前缀
        if flag == 1:
            newName = "python_"+i
        # 删除前缀
        elif flag == 2:
            num = len("python_")
            newName = i[num:]
        os.rename(i, newName)
print(os.listdir())
    
