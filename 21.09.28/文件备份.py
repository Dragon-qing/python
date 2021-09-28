# 用户输入目标文件
old_name = input("请输入要备份的文件名")
print(old_name)
index = old_name.rfind(".")
if index > 0:
    postfix = old_name[index:]
new_name = old_name[:index] + "(备份)" + postfix
print("new_name=%s" % (new_name))
old_f = open(old_name, "rb")
new_f = open(new_name, "wb")
while True:
    con = old_f.read(1024)
    new_f.write(con)
    if len(con) == 0:
        break
old_f.close()
new_f.close()
