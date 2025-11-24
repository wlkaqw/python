def fun01(m,n):
    price=0.5*m+0.3*n
    return int(price)


def fun02(year,month):
    def is_leap(year):
        """判断一个年份是否为闰年"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 0  # 无效月份


def fun03(salary):
    # 全年起征点
    threshold = 60000
    taxable_income = salary - threshold

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


def fun04(list):
    re=[]
    for num in list:
        a=num
        i=num
        sum=0
        while i>0:
            b=i%10
            i//=10
            sum+=b
        if a%sum==0:
            re.append(a)
    re.sort(reverse=True)
    return re



def GetElementCount(n):
    c = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            c += 1
    return c


def MyCompare(n):
    return [-GetElementCount(n), n]


def fun07(lst):
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


def fun08(lst):
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
    print(fun04([4032, 2473, 2924, 4972, 2992, 1680, 402, 1011, 3544, 1306]))

    pass