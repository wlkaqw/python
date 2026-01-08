import math
def func901(f0,f1,num):
    lst=[f0,f1]
    for i in range(num):
        lst.append(lst[-1]+lst[-2])
    return lst[num]

def func902(lst,x):
    if not lst:
        lst1=[i for i in lst if i>=x]
        lst2=[i for i in lst if i<x]
        return lst1+lst2
    else:
        return []
    
def semi_prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

def func903(n):
    lst1=[]
    for i in range(10,n+1):
        if semi_prime(i):
            lst1.append(i)
    return sum(lst1)

def func904(lst):
    return sorted(lst,key=lambda x:-len(str(abs(x))))

def func905(lst):
    return sorted(lst, key=lambda x:(-int(str(abs(x))[0]),x))

def func906(n):
    count=0
    for i in range(-1,-len(str(math.factorial(n)))-1,-1):
        if str(math.factorial(n))[i]=='0':
            count+=1
        else:
            break
    return count

def sum_(n):
    return sum(int(str(n)[i]) for i in range(0,len(str(n))))

def func907(lst):
    if not lst:
        return []
    return sorted([i for i in lst if i %2!=0], key=lambda x: (sum_(x),-x))+sorted([i for i in lst if i %2==0], key=lambda x: (sum_(x),-x))

def func908(lst):
    max_=max(str(bin(i)).count('1') for i in lst)
    return sorted([i for i in lst if str(bin(i)).count('1')==max_], key=lambda x: -x)

def func909(tup,num):
    return tuple(sorted([i for i in tup if sum_(i)>=num], reverse=True))+tuple(sorted([i for i in tup if sum_(i)<num]))

def func910(tp):
    if not tp:
        return () 
    str1=''.join(str(tp).split(', '))
    max_=max(str1.count(c) for c in str1)
    return tuple(sorted(set([int(c) for c in str1 if str1.count(c)==max_])))

def inz(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count

def func911(tp):
    if not tp:
        return ()
    dic={}
    for i in tp:
        dic[inz(i)]=dic.get(inz(i),[])+[i]
        dic[inz(i)].sort()
    return tuple(sorted(dic.items(), key=lambda x: -x[0]))
    
def func912(dict1):
    dict2={}
    for i in dict1.keys():
        dict2[i]=max(dict1[i])
    return dict2

def func913(dic1):
    dic={}
    for i in range(4):
        max_=max([x[i] for x in dic1.values()])
        dic[max_]=sorted([k for k,v in dic1.items() if v[i]==max_])
    return dic

def func914(lst):
    return tuple(sorted(set.intersection(*[set(i) for i in lst])))


def func915(lst):
    dic={}
    lst1=[item for i in lst for item in i]
    for i in lst1:
        dic[i]=dic.get(i,0)+1
    return dic

def func916(dicGroups,studentID):
        return tuple(sorted([x for x in dicGroups.keys() if studentID in dicGroups[x]]))


print(func905([20, 984, -8, 987, 827,477, 797, 550,509, 487, 318, 353]))
print(func906(9))
print(func907([627, 517, 990, 26, 275, 704, 148, 998,371]))
print(func908([750, 146, 177, 354, 378, 260, 130, 71,105, 368, 435, 950]))
print(func909((2492, 1353, 6717, 2430, 8316, 8006,3134, 840, 816, 3738) , 20))
print(func910(((5875, 7367, 4784, 4470, 413, 8631,3568, 7886, 9078, 3623))))
print(func911((3148, 9078, 1520, 4762, 7341, 3845,1888, 8435, 2696, 9000, 8074, 8488,3781)))
print(func912({1006: (77, 77, 90, 95, 75, 84, 91, 78,91, 77), 1000: (96, 93, 87, 84, 99, 90,88, 85, 85, 97), 1001: (87, 82, 92, 89,95, 87, 74, 71, 86, 79)}))
print(func913({1035: (99, 98, 92, 79), 1031: (70, 93,84, 71), 1019: (74, 82, 74, 95), 1040:(86, 77, 90, 90), 1039: (80, 82, 73, 76),1016: (99, 86, 86, 100), 1025: (71, 77,80, 77), 1009: (74, 84, 83, 87), 1036:(74, 88, 74, 94), 1004: (85, 78, 90, 100)}))
print(func914([{1000, 1001, 1002, 1005}, {1001,1002, 1004, 1005}, {1000, 1001, 1002,1004, 1005}, {1000, 1001, 1002, 1003,1004, 1005}, {1000, 1001, 1004, 1005},{1000, 1001, 1002, 1003, 1004, 1005},{1000, 1001, 1002, 1003, 1004, 1005}]))
print(func915([{1009,1004,1005,1007},{1009,1002},{1008,1010,1003,1006},{1000,1002,1003},{1000,1002,1004,1007,1008,1009},{1002,1004,1007},{1001,1010,1002,1006},{1000,1002,1003,1005}]))
print(func916({1008: [37, 19, 1, 13, 3, 39], 1006: [12,26, 37, 30, 10, 21], 1001: [12, 36, 15]} ,12))
