# from random import randint
import random

# 摇奖函数
def random_bets():
    print("摇奖中---------")
    redBall = range(1,34)
    select_redBall = random.sample(redBall, 6)
    select_buleBall = random.randint(1,16)
    # ↓测试数据，测试完请注释掉↓
    # select_redBall = [1,2,3,4,5,6]
    # select_buleBall = 1
    select_wardTuple = (select_redBall, select_buleBall)
    print("------ 摇奖结果 ------")
    for j in range(6):
        print("%02d"%select_redBall[j], end=' ')
    print("| %02d\n\n"%select_buleBall)
    return select_wardTuple

# 随机下注函数
def drawLottery():
    i = 0
    redBall = []
    for i in range(6):
        num = random.randint(1,33)
        redBall.append(num)
    blueBall = random.randint(1,16)
    # ↓测试数据，测试完请注释掉↓
    # redBall = [2,3,15,12,32,6]
    # blueBall = 6
    tuple_ward = (redBall, blueBall)
    return tuple_ward

# 兑奖函数
def reward(tuple_ward = ([0, 0, 0, 0, 0, 0], 0), tuple_Reward = ([0, 0, 0, 0, 0, 0], 0)):
    redCorrect  = 0
    blueCorrect = 0
    award_level = 0
    for m in range(6):
        if tuple_ward[0][m] == tuple_Reward[0][m]:
            redCorrect += 1
    if tuple_ward[1] == tuple_Reward[1]:
        blueCorrect += 1
    # redCorrect  = random.sample((3,4,5), 1)[0]
    if redCorrect == 6 and blueCorrect == 1:
        award_level = 1
    elif redCorrect == 6 and blueCorrect == 0:
        award_level = 2
    elif redCorrect == 5 and blueCorrect == 1:
        award_level = 3
    elif redCorrect == 5 or (redCorrect == 4 and blueCorrect == 1):
        award_level = 4
    elif redCorrect == 4 or (redCorrect == 3 and blueCorrect == 1):
        award_level = 5
    elif blueCorrect == 1:
        award_level = 6
    if award_level != 0:
        for j in range(6):
            print("%02d"%tuple_Reward[0][j], end=' ')
        print("| %02d"%tuple_Reward[1])
        
    return award_level

# 机选下注
def machineBet(num = int(input("请输入机选下注数:"))):
    selectWard_list = [0]*num
    for i in range(num):
        selectWard_list[i] = drawLottery()
    return selectWard_list



# 显示下注情况
def display(betList = []):
    print("------ 下注情况 ------")
    for i in range(len(betList)):
        for j in range(6):
            print("%02d"%(betList[i][0][j]), end=' ')
        print("| %02d"%betList[i][1])

def main():
    # 开始下注，接收下注信息 层次关系--list[tuple(list[int])]
    selectWard_list = machineBet()
    # 显示下注情况
    display(selectWard_list)
    # 开始摇奖
    select_wardTuple = random_bets()
    # 验证是否中奖
    for x in range(len(selectWard_list)):
        ward_level = reward(select_wardTuple, selectWard_list[x])
        if ward_level != 0:
            print("恭喜您！第{}注中了{}等奖".format(x+1, ward_level))

main()


# ward = drawLottery()
# Reward = drawLottery()
# print(ward)
# print(Reward)
# level = reward(ward, Reward)
# print(level)

# redBall = [1, 2, 3, 4, 5, 6]
# ReredBall = [1, 2, 4, 14, 5, 6]
# tuple_ward = (redBall, 0)
# tuple_Reward = (ReredBall, 0)
# level= reward((redBall,2), (ReredBall, 2))
# print(level)
