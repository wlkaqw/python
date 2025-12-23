import math
def func1(rec1, rec2):
    x1_1, y1_1, x2_1, y2_1 = rec1  # 0, 2, 4, 6
    x1_2, y1_2, x2_2, y2_2 = rec2  # 2, 0, 6, 4
    
    # x轴判断：rec1左 < rec2右 (0 < 6) 且 rec2左 < rec1右 (2 < 4) → True
    x_overlap = (x1_1 < x2_2) and (x1_2 < x2_1)
    # y轴判断：rec1下 < rec2上 (2 < 4) 且 rec2下 < rec1上 (0 < 6) → True
    y_overlap = (y1_1 < y2_2) and (y1_2 < y2_1)
    
    return x_overlap and y_overlap  # True and True → 返回True

def func2(rate,money,years):
    pass

def func3(m,n):
    # 确定区间的上下边界
    low = min(m, n)
    high = max(m, n)
    
    # 小于2的区间无质数
    if high < 2:
        return 0
    
    # 埃拉托斯特尼筛法：生成2到high的质数表
    is_prime = [True] * (high + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    for i in range(2, int(high ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : high+1 : i] = [False] * len(is_prime[i*i : high+1 : i])
    
    # 统计[low, high]内的质数数量
    count = 0
    for num in range(max(low, 2), high + 1):  # 从2开始统计（low可能小于2）
        if is_prime[num]:
            count += 1
    return count

def func4(lst):
    # 列表长度不足2，无法交易
    if len(lst) < 2:
        return 0
    
    min_price = lst[0]
    max_profit = 0
    
    for price in lst[1:]:
        # 更新最低买入价
        if price < min_price:
            min_price = price
        # 计算当前利润并更新最大利润
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    
    return max_profit
  
def func5(scoreDic,x):
    # 步骤1：统计每门课程的总分、参与人数、以及成绩≥x的人数
    course_stats = {}  # 结构：{课程编号: {"total": 总分, "count": 参与人数, "pass_count": 达标人数}}
    for stu_id, stu_courses in scoreDic.items():
        for course_id, score in stu_courses.items():
            # 初始化课程统计信息
            if course_id not in course_stats:
                course_stats[course_id] = {"total": 0, "count": 0, "pass_count": 0}
            # 累计总分和参与人数
            course_stats[course_id]["total"] += score
            course_stats[course_id]["count"] += 1
            # 统计成绩≥x的人数
            if score >= x:
                course_stats[course_id]["pass_count"] += 1
    
    # 步骤2：筛选平均分（整数部分）≥x的课程，并构建结果字典
    result = {}
    for course_id, stats in course_stats.items():
        avg = stats["total"] // stats["count"]  # 整数部分（地板除）
        if avg >= x:
            result[course_id] = stats["pass_count"]
    
    return result

def inz(n):
    lst1=[]
    for i in range(2,n):
        if n%i==0:
            lst1.append(i)
    return lst1

def func6(lst):
    lst1=[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j:
                continue
            if len(set(inz(lst[i])) & set(inz(lst[j])))>=2:
                break
        else: 
            lst1.append(lst[i])
    return sorted(lst1)


def func7(strn, t):
    str1=''
    for i in strn:
        if i.isdigit():
            if t[0]<=int(i)<=t[1]:
                str1+=i
    if str1=='':
        return []
    lst1=inz(int(str1))
    lst1.append(int(str1))
    lst1.insert(0,1)
    return lst1

def func8(s):
    if len(s) < 8:
        return False
    has_digit = False
    has_lower = False
    has_upper = False
    
    for char in s:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
    same = False
    for i in range(len(s)-2):
        if s[i]==s[i+1]==s[i+2]:
            same = True
            break
    return has_digit and has_lower and has_upper and not same

if __name__ == "__main__":
    print(func1([0,2,4,6], [2,0,6,4]))
    print(func3(-5,11))
    print(func5({2501: {102: 62, 103: 83, 104: 44, 105: 73}, 2502: {101: 48, 103: 63, 104: 74, 105: 54}, 2503: {101: 56, 103: 38, 104: 98, 105: 41}, 2504: {101: 51, 102: 53, 103: 73, 104: 55, 105: 53}, 2505: {101: 70, 102: 60, 103: 45, 104: 73, 105: 91}}, 60))
    print(func6([39, 180, 123, 195, 156, 22, 91, 133, 26, 184]))  # [22, 91, 123, 133]
    print(func6([80, 84, 94, 188, 136, 68])) #[]
    print(func7("1a2b3.54x",(2, 4)))
    print(func7("1a2b3.54x",(7, 9)))
    print(func8("Claimed78"))  # True
    print(func8("remains"))  # False