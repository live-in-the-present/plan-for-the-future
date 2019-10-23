# 导入工具包
# 注意：在导入工具包的时候，应该将导入的语句放在文件顶部
import random

#从控制台输入要出的拳：石头（1），剪刀（2），布（3)
player = int(input("请出拳：石头（1），剪刀（2），布（3):"))

#电脑随机出拳，先假定电脑只会出石头
computer = random.randint(1, 3)
print("你出的拳是%d - 电脑出的拳是%d" % (player,computer))

#比较胜负
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("你赢了，电脑输了！")

elif player == computer:
    print("平局，再来")

else:
    print("你输了，电脑赢了，，，，")