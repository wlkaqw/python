def func301(A,B):
    list=A+B
    return list[7:15]

def func302(A):
    return sorted(A)[int(0.5*(len(A)-0.5))]

def func303(A):
    return 1 if A == A[::-1] else 0

def func304(A):
    return list(set(A))

def func305(A):
    return [item for item in A if isinstance(item, int)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def func306(A):
    primes = [num for num in A if is_prime(num)]
    count = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            s = primes[i] + primes[j]
            if s in primes:
                count += 1
    return count

def func307(A):
    result = []
    current,count = A[0], 1
    #遇到下一个不同的元素，添加上一个元素
    for num in A[1:]:
        if num == current:
            count += 1
        else:
            result.append(current * count if count >= 2 else current)
            current, count = num, 1
    #处理最后一个元素
    result.append(current * count if count >= 2 else current)
    return result

def func308(lst):
    even = sum(1 for num in lst if num % 2 == 0)
    odd = len(lst) - even
    if even == odd:
        return 1
    elif even > odd:
        return 2
    else:
        return 3

def func309(lst):
    # 计算每个学生的总分，并存储为[学号, 总分]的格式
    students = [[stu[0], stu[1] + stu[2]] for stu in lst]
    # 先按总分降序排序，再按学号升序排序
    students.sort(key=lambda x: (-x[1], x[0]))
    # 找到最高总分
    max_score = students[0][1]
    # 筛选出总分等于最高总分的学生
    result = [stu for stu in students if stu[1] == max_score]
    return result

def func310(Num):
    if Num < 2:
        return []
    primes = []
    for num in range(2, Num + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
   
def func311(A):
    result = []
    for num in A:
        if num == 0:
            result.append(0)
        else:
            while num > 0:
                result.append(num % 10)
                num = num // 10
    return result

def func312(lst):
    if len(lst) < 2:
        return []
    list = lst.copy()
    while len(list) > 2:
        place = 0
        sum = 0
        for i in range(len(list)-1):
            current_sum = list[i] + list[i + 1]
            if current_sum > sum:
                sum = current_sum
                place = i
        new = sum//2
        list = list[:place] + [new] + list[place + 2:]
    return list

def func313(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def get_digit_avg(num):
    s = str(num)
    digit_sum = sum(int(c) for c in s)
    return digit_sum / len(s)

def func314(A):
    return sorted(A, key=lambda x: (get_digit_avg(x), -x))

def func315(A,Num):
    for i in range(len(A)):
        if Num <= A[i]:
            A.insert(i, Num)
            return A
    A.append(Num)
    return A

if __name__=="__main__":
    print(func310(10))