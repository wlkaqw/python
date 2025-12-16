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

def func6():
    

#print(func2([2,7,11,15],9))
#print(func3([1,5,7,9],[2,3,4,6,8,10]))
#print(func4(29))
print(func5(284,220))