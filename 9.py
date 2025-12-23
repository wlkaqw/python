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
    if not tp:
        return ()
    dic={}
    str1=''
    for i in tp:
        str1+=str(i)
    for i in range(1,10):
        dic[i]=str1.count(str(i))
    max_count = max(dic.values())
    lst1=sorted([k for k, v in dic.items() if v == max_count])
    return tuple(lst1)

def inz(n):
    if n==1:
        return 1
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return len(lst)

def func911(tp):
    dic={}
    for i in tp:
        count=inz(i)
        if count not in dic:
            dic[count]=[]
        dic[count].append(i)
    for i in dic:
        dic[i].sort()
    return tuple(sorted(dic.items(),key=lambda x:-x[0]))

def func912(dict):
    dic={}
    for i in dict:
        max_=max(dict[i])
        dic[i]=max_
    return dic

def func913(dict):
    if not dict:
        return ()
    res=[]
    for i in range(4):
        lst1=[]
        for id,scores in dict.items():
            lst1.append((scores[i],id))
        max_score=max(x[0] for x in lst1)
        top_id=sorted(id for score,id in lst1 if score==max_score)
        res.append((max_score,top_id))
    return tuple(res)

def func914(lst):
    lst1=[]
    for i in lst:
        for j in i:
            if j not in lst1:
                lst1.append(j)
    res=[]
    for j in lst1:
        for i in lst:
            if j not in i:
                break
        else:
            res.append(j)
    return tuple(sorted(res))




print(func901(7,4,16))
print(func902([],4))
print(func903(16))
print(func904([39,-498,1]))
print(func905([20,984,-8,987,827,477,797,550,509,487,318,353]))
print(func906(36))
print(func907([627,517,990,26,275,704,148,998,371]))
print(func908([750,146,177,354,378,260,130,71,105,368,435,950]))
print(func909((2392,1353,6717,2430,8316,8006,3134,840,16,3738),20))
print(func910((9391, 5644, 3085, 2201, 7182, 4985,7843, 6369, 904, 9810, 3836, 3321, 979)))
print(func911((3148, 9078, 1520, 4762, 7341, 3845,1888, 8435, 2696, 9000, 8074, 8488,3781)))
print(func912({1006: (77, 77, 90, 95, 75, 84, 91, 78,91, 77), 1000: (96, 93, 87, 84, 99, 90,88, 85, 85, 97), 1001: (87, 82, 92, 89,95, 87, 74, 71, 86, 79)}))
print(func913({1035: (99, 98, 92, 79), 1031: (70, 93,84, 71), 1019: (74, 82, 74, 95), 1040:(86, 77, 90, 90), 1039: (80, 82, 73, 76),1016: (99, 86, 86, 100), 1025: (71, 77,80, 77), 1009: (74, 84, 83, 87), 1036:(74, 88, 74, 94), 1004: (85, 78, 90, 100)}))
print(func914([{1000, 1001, 1002, 1005}, {1001,1002, 1004, 1005}, {1000, 1001, 1002,1004, 1005}, {1000, 1001, 1002, 1003,1004, 1005}, {1000, 1001, 1004, 1005},{1000, 1001, 1002, 1003, 1004, 1005},{1000, 1001, 1002, 1003, 1004, 1005}]))