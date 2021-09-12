import random
# computer
computer = random.randint(0, 2)
# player
player = int(input("请输入(0--石头，1--剪刀，2--布)"))
if ((player == 0)and(computer == 1)) or ((player == 1)and(computer == 0)) or ((player == 2)and(computer == 1)):
    print("win")
elif player == computer:
    print("平")
else:
    print("loss")
print(computer)
