# 随机分配办公室
import random
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[], [], []]
for name in teachers:
    number = random.randint(0, 2)
    offices[number].append(name)
# print (offices)
for office in offices:
    print(f"办公室人数是{len(office)},人员为{office}")
