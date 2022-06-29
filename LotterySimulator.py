#  仅供娱乐
import random, time

# Define which mode you would like to play
mode = input("选择模式：\n \
    a - 幸运5+2\n \
    b - 非常6+1\n")

# Define the red ball qty which need to pick
str_RedBallQty = input("输入需要摇取的红球的个数:\n")
redBallQty = int(str_RedBallQty)

# Define the blue ball qty which need to pick
str_BlueBallQty = input("输入需要摇取的蓝球的个数:\n")
blueBallQty = int(str_BlueBallQty)

# Define the max interval time in s for random
str_maxTime = input("输入随机间隔时, 默认为5s:\n")
maxTime = int(str_maxTime)

if mode == 'a':
    redMaxNum = 33
    blueMaxNum = 16
else:
    redMaxNum = 35
    blueMaxNum = 12


redBallArr = []
blueBallArr = []

def sleepTime(maxTime = 5):
    time.sleep(random.randint(1, maxTime))

def normArr(qty, maxNum, maxTime):
    ballArr = []
    while len(ballArr) < qty:
        sleepTime(maxTime)
        ball = random.randint(1, maxNum)
        if ball not in ballArr:
            ballArr.append(ball)
            if maxNum >= 33:
                print(str(len(ballArr)) + "号红球号码：" + str(ball))
                redBallArr.append(ball)
            else:
                print(str(len(ballArr)) + "号蓝球号码：" + str(ball))
                blueBallArr.append(ball)

def repoNum(redBallArr, blueBallArr):
    print("红球序列: " + str(redBallArr))
    print("蓝球序列: " + str(blueBallArr))

normArr(redBallQty, redMaxNum, maxTime)
sleepTime(maxTime)
normArr(blueBallQty, blueMaxNum, maxTime)
sleepTime(maxTime)
repoNum(redBallArr, blueBallArr)
