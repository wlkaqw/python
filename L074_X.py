def func2(lst,num):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==num:
                return[i,j]

def func3(lst1,lst2):
    return sorted(lst1+lst2)

def func4(n):
    if n not in range(1,1001):
        return None
    for i in range(1,1000):
        sum1=0
        for j in range(i,i+n+1):
            sum1+=j**2
        sum2=0
        for k in range(i+n+1,i+2*n+1):
            sum2+=k**2
        if sum1==sum2:
            return list(range(i,i+2*n+1))
            break
    else:
        return None

def func5(n1,n2):
    lst1=[]
    lst2=[]    
    for i in range(1,n1):
        if n1%i==0:
            lst1.append(i)
    for i in range(1,n2):
        if n2%i==0:
            lst2.append(i)
    sum1=0
    sum2=0
    for i in lst1:
        sum1+=i
    for i in lst2:
        sum2+=i
    if sum1==n2 and sum2==n1:
        return True
    else:
        return False

def func6(lst):
    ave=sum(lst)/len(lst)
    res=[]
    for i in lst:
        if i>ave:
            res.append(i)
    return res
    
def func7(lst,index):
    lst1=lst[:index]
    lst2=lst[index+1:]
    res=list(reversed(lst1))+[lst[index]]+list(reversed(lst2))
    return res

def func8(lst):
    lst1=[]
    max_=max(lst)
    for i in range(len(lst)):
        if lst[i]==max_:
            lst1.append(i)
    lst1.insert(0,max_)
    return lst1

def is_prime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def func9(n):
    if n<=2:
        return []
    lst1=[]
    for i in range(3,int(n*0.5),2):
        if is_prime(i) and is_prime(n-i):
            lst1.append((i,n-i))
    return lst1

def func10(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if type(i)==float:
            lst1.append(i)
    for i in lst:
        if type(i)==int:
            lst2.append(i)
    lst3=sorted(lst1,reverse=True)+sorted(lst2,reverse=True)

#print(func2([2,7,11,15],9))
#print(func3([1,5,7,9],[2,3,4,6,8,10]))
#print(func4(29))
#print(func5(284,220))
#print(func6([1,3,5,7,9]))
#print(func7([1,2,3,4,5,6,7,8,9],4))
#print(func8([1,2,3,4,5,6,6,6]))
#print(func9(64))