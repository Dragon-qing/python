name_list = ["Tom", "Lily", "Rose"]
name = input("请输入用户名：")
number = 0
for i in name_list:
    name_list[number] = i.upper()
    number += 1
for i in name_list:
    print(i)
if name.upper() in name_list:
    print("您输入的用户名已存在")
else:
    print("succeed!!!")