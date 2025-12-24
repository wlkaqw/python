import math
def func901(f0,f1,num):
    lst=[f0,f1]
    if num<=0:
        return None
    num_=num
    while num_>1:
        a=lst[-1]+lst[-2]
        lst.append(a)
        num_-=1
    return lst[num]

def func902(lst,x):
    lst1=[]
    lst2=[]
    for i in lst:
        if i>=x:
            lst1.append(i)
        else:
            lst2.append(i)
    return lst1+lst2

def inz(n):
    lst=[]
    for i in (2,n):
        if n%i==0:
            lst.append(i)
    if len(lst)>=2:
        return False
    else:
        return True

def func903(n):
    lst=[]
    for i in range(10,n+1):
        if inz(i):
            lst.append(i)
    return sum(lst)

def func904(lst):
    return sorted(lst,key=lambda x:-len(str(abs(x))))

def func905(lst):
    return sorted(lst,key=lambda x:(-int(str(abs(x))[0]),x))

def func906(n):     #n!末尾的0由2*5的对数决定，2的数量远多于5，只需统计因子5的个数
    if n<1:
        return 0
    num=0
    while n>0:
        n//=5
        num+=n
    return num

def sum_(n):
    count=0
    for i in range(len(str(n))):
        count+=int(str(n)[i])
    return count

def func907(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if i%2==0:
            lst2.append(i)
        else:
            lst1.append(i)
    lst1=sorted(lst1,key=lambda x:(sum_(x),-x))
    lst2=sorted(lst2,key=lambda x:(sum_(x),-x))
    return lst1+lst2

def bin_(n):
    return str(bin(n)).count('1')

def func908(lst):
    dic={}
    max_=max([bin_(x) for x in lst])
    lst1=[]
    for i in lst:
        if bin_(i)==max_:
            lst1.append(i)
    return sorted(lst1,reverse=True)    

def func909(tp,num):
    lst1=[]
    lst2=[]
    for i in tp:
        if sum_(i)>=num:
            lst1.append(i)
        else:
            lst2.append(i)
    lst1.sort(reverse=True)
    lst2.sort(reverse=False)
    return tuple(lst1+lst2)

def func910(tp):
    dic={}
    str1=''.join(str(tp))
    for i in range(10):
        dic[i]=str1.count(str(i))
    lst1=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    max_=lst1[0][0]
    lst2=[]
    for i in lst1:
        if i[1]==max_:
            lst2.append(i[0])
    lst2.sort()
    return tuple(lst2)

print(func901(7,4,16))
print(func902([],4))
print(func903(16))
print(func904([39,-498,1]))
print(func905([20,984,-8,987,827,477,797,550,509,487,318,353]))
print(func906(36))
print(func907([627,517,990,26,275,704,148,998,371]))
print(func908([750,146,177,354,378,260,130,71,105,368,435,950]))
print(func909((2392,1353,6717,2430,8316,8006,3134,840,16,3738),20))
print(func910((5875,7367,4784,4470,413,8631,3568,7886,9078,3623)))