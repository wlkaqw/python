import math
from itertools import count


def func1(m1, m2):
    price = 0.5 * m1 + 0.3 * m2
    return int(price)

def is_leap(year):
    """判断一个年份是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def func2(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 0  # 无效月份


def func3(annual_salary):
    # 全年起征点
    threshold = 60000
    taxable_income = annual_salary - threshold

    # 如果应纳税所得额不超过0，无需缴税
    if taxable_income <= 0:
        return 0

    # 税率区间配置：(上限, 税率, 速算扣除数)
    tax_brackets = [
        (36000, 0.03, 0),
        (144000, 0.1, 2520),
        (300000, 0.2, 16920),
        (420000, 0.25, 31920),
        (660000, 0.3, 52920),
        (960000, 0.35, 85920),
        (float('inf'), 0.45, 181920)
    ]

    # 找到对应的税率区间并计算税额
    for upper_limit, rate, deduction in tax_brackets:
        if taxable_income <= upper_limit:
            tax = taxable_income * rate - deduction
            return int(tax)

    # 理论上不会执行到这里，作为安全保障
    return 0


def func4(lst):
    re = []
    for num in lst:
        a = num
        i = num
        sum = 0
        while i > 0:
            b = i % 10
            i //= 10
            sum += b
        if a % sum == 0:
            re.append(a)
    re.sort(reverse=True)
    return re


def func5(left, right):
    if left > right:
        left, right = right, left
    count = 0
    for i in range(left, right+1):
        num = len(str(i))
        if i == i**2%(10**num):
            count += 1
    return count

def func6(lst):
    result = -1
    for i in lst:
        one = i%10
        ten = (i//10)%10
        hundred = i//100
        if ten %2 == 0 and hundred %2 == 0 and (one + ten +hundred) %2 ==1 :
            result = i
    return result

def GetElementCount(n):
    c = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            c += 1
    return c

def MyCompare(n):
    return [-GetElementCount(n), n]

def func7(lst):
    lst.sort(key=MyCompare)
    return lst

def IsReplace(lst1, lst2):
    flag = 0
    for i in range(len(lst1)):
        if lst2[i] < lst1[i]:
            break
        if lst2[i] > lst1[i]:
            flag = 1
    else:
        if flag == 1:
            return True
    return False

def func8(lst):
    res = []
    for a in lst:
        for b in lst:
            if a is not b:
                if IsReplace(a, b):
                    break
        else:
            res.append(a)
    return res


if __name__ == "__main__":
    print(func8([[78, 53], [60, 10], [49, 55], [69, 39], [57, 89]]))

