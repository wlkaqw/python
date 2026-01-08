import math
import random
def func3(lst):
    lst1=lst[::2]
    lst1.sort(reverse=True)
    lst[::2]=lst1
    return lst

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def func9(lst):
    return sorted(lst[:10])+list(reversed(lst[10:]))

def func13():
    x=[random.randint(1,20) for i in range(50)]
    dic={}
    for i in x:
        dic[i]=dic.get(i,0)+1
    print(dic)

def func19():
    x=list(range(20))
    for index,value in enumerate(x):
        if value ==3:
            x[index]=5
    return x

def func20():
    x=[range(3*i,3*i+5)for i in range(2)]
    x=list(map(list,x)) #2行5列的二维列表，可看作矩阵
    x=list(map(list,zip(*x)))#*x解包操作，将x的子列表作为独立参数传递给zip。zip按列取元素，生成5个2元素的元组，最后转置为5行2列

def func26(n):
    b_n=bin(n)
    index=b_n.rfind('1')+1
    return len(b_n[index:])

def func27(n):#n个人比赛，计算至少多少场比赛能决出冠军，答案是n-1
    if n==1:
        return 0
    if n==2:
        return 1
    m,c=divmod(n,2)#divmod(被除数，除数)＝商，余数
    return m+func27(c+m)

def func29(s):#找只出现一次的字符
    dic={}
    for ch in s:
        dic[ch]=dic.get(ch,0)+1
    return [ch for ch,n in dic.items() if n==1]

def func31(strNumber):#去掉千位分隔符
    if strNumber != '0':
        return ''.join(strNumber.split(','))
    else:
        pass
        
def func32(strNumber):
    parts=strNumber.split('.',1)
    if not all(part.isdigit() for part in parts):
        return '无效数字'
    def nested(s):
        result=[]
        index=len(s)%3
        if index !=0:
            result.append(s[:index])
        for i in range(index,len(s),3):
            result.append(s[i:i+3])
        return ','.join(result)
    first=nested(parts[0])
    second=parts[1]
    second=''.join(reversed(nested(''.join(reversed(second)))))
    return '.'.join([first,second]).strip(',0')



print(func3([1,9,4,7,2,3,6,9,0,14,23,54,89,32,41,6]))
print(func9([1,9,4,7,2,3,6,9,0,14,23,54,89,32,41,6,32,74,99,16]))
print(func13())
print(func26(64))
print(func27(8))
print(func29('cbdhwivbeiqdiosabcdhvvieqbuochnsioanxkANPCIWHQIOHVCOIEQBVIRBIHWQCBIJSABHBXSbvhriwbv'))
print(func31('1,234,567'))
print(func32('0283746.3376'))
print(10/2)