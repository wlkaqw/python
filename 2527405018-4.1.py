# -*- codeing = utf-8 -*-
import random
import math


def func4101(num):
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"


def func4102(num):
    if not (0 <= num <= 100):
        return "输入的数不在[0-100]范围内"
    else:
        return num % 3 == 0


def func4103(num):
    num_str = str(num)
    digit_count = len(num_str)
    digits = [int(char) for char in num_str]
    reversed_str = num_str[::-1]
    return digit_count,digits,reversed_str


def func4104(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2


def func4105(num1,num2,num3):
    sorted_nums = sorted([num1,num1,num3])
    return sorted_nums


def func4106(username, password):
    user_info = [("user1", "password1"), ("user2", "password2"), ("user3", "password3")]
    if (username, password) in user_info:
        return "登录成功"
    else:
        return "用户名或密码不正确"


def func4107(N):
    price = 15
    # 先计算不考虑促销时能买的瓶数
    base = N // price
    if base == 0:
        return 0
    # 分别计算两种促销方式能获得的额外瓶数，取最优
    # 买5送2的促销：每买5瓶送2瓶，即每7瓶花费5*15=75元
    five_promotion = (base // 5) * 2
    remaining_after_five = base % 5
    # 买3送1的促销：在买5送2剩余的基础上，每买3瓶送1瓶
    three_promotion = (remaining_after_five // 3) * 1
    total = base + five_promotion + three_promotion
    return total


def func4108(deposit):
    if deposit < 100000:
        rate = 0.015
    elif 100000 <= deposit < 500000:
        rate = 0.02
    elif 500000 <= deposit < 1000000:
        rate = 0.03
    else:
        rate = 0.035
    total = deposit * (1 + rate)
    return total


def func4109(x1,y1,x2,y2,x3,y3):
    a = math.  t((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    if a + b > c and a + c > b and b + c > a:
        # 计算周长
        perimeter = a + b + c
        # 用海伦公式计算面积
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area, perimeter
    else:
        return "不能构成三角形"


def func4110(x1,y1,x2,y2,x3,y3):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    # 修正浮点误差，将三边长度四舍五入
    a = round(a, 9)
    b = round(b, 9)
    c = round(c, 9)

    # 判断能否构成三角形
    if a + b > c and a + c > b and b + c > a:
        # 判断等边三角形：三边相等
        if a == b ==c:
            return "等边三角形"
        # 判断直角三角形：满足勾股定理（三边平方和关系）
        elif (abs(a ** 2 + b ** 2 - c ** 2) < 1e-9) or (abs(a ** 2 + c ** 2 - b ** 2) < 1e-9) or (
                abs(b ** 2 + c ** 2 - a ** 2) < 1e-9):
            return "直角三角形"
        # 其他三角形
        else:
            return "一般三角形"
    else:
        return "不能构成三角形"


def func4111(x1,y1,r,x2,y2):
    # 计算点到圆心的距离的平方
    distance_square = (x2 - x1) ** 2 + (y2 - y1) ** 2
    # 计算半径的平方
    r_square = r ** 2
    if distance_square <= r_square:
        return f"点({x2}, {y2})在圆内"
    else:
        return f"点({x2}, {y2})在圆外"


def func4201():
    pass

def func4202():
    pass


def func4203():
    pass


def func4204():
    pass

if __name__ == '__main__':
   pass



