#假设有r = 1的四个圆其圆心分别位于（2，2），（2，-2），（-2，2），（-2，-2）
#有一任意点A（x,y),判断其是否在圆内

r = 1 #圆半径为1

def distance(x,y):

    a = b = 2 #圆心坐标绝对值
    if x > 0:
        a = -a
    if  y > 0:
        b = -b

    dist = (abs(a-2)**2 + abs(b-2)**2) ** 0.5 #计算点于对应象限圆心的距离

    point = "(" + str(x) + "," + str(y) + ")"
    if dist > r: #判断距离是否大于r
        print("The point A" + point + " is not in the circle")
    else:
        print("The point A" + point + " is not in the circle")

x = float(input("Please input x of A: "))
y = float(input("Please input y of A: "))

distance(x,y)
