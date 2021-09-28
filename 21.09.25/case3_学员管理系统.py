# 显示功能界面
import os
info = []


def info_print():
    """
    功能菜单
    :return:
    """
    print("请选择功能")
    print("-"*20)
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.查询学员")
    print("5.显示所有学员")
    print("6.退出系统")
    print("-"*20)


def add_info():
    """
    添加学员信息
    :return:
    """
    new_id = int(input("请输入学号："))
    new_name = input("请输入学员姓名：")
    new_gender = input("请输入学员性别：")
    global info
    for i in info:
        if i["id"] == new_id:
            print("学号重复，添加失败")
            return
    new_dict = dict()
    new_dict["id"] = new_id
    new_dict["name"] = new_name
    new_dict["gender"] = new_gender
    info.append(new_dict)


def del_info():
    """
    删除学员
    :return:
    """
    id_del = int(input("请输入要删除学员的学号"))
    global info
    for i in info:
        if id_del == i["id"]:
            info.remove(i)
            break
    else:
        print("学员不存在")


def update_info():
    """
    修改学员信息
    :return:
    """
    id_update = int(input("请输入要修改的学员学号："))
    global  info
    for i in info:
        if id_update == i["id"]:
            name_updated = input("请输入要更改的学员姓名：")
            i["name"] = name_updated
            break
    else:
        print("学员不存在")


def find_info():
    """
    查找学员信息
    :return:
    """
    id_find = int(input("请输入要查询的学员学号："))
    for i in info:
        if i["id"] == id_find:
            print(i)
            break
    else:
        print("学员不存在")


def all_info():
    """查询所有学员信息"""
    if len(info) == 0:
        print("无学员信息")
    else:
        print("学号\t姓名\t性别")
        for i in info:
            print(f"{i['id']}\t{i['name']}\t{i['gender']}")


while True:
    info_print()

    user_num = int(input("请输入功能序号："))
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        update_info()
    elif user_num == 4:
        find_info()
    elif user_num == 5:
        all_info()
    elif user_num == 6:
        exit_flag = input("exit? yes/no:")
        if exit_flag == "yes":
            break
    else:
        print("输入的功能序号有误")
    os.system("pause")
