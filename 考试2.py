import math
def func1(rec1,rec2):
    pass

def func2(rate,money,years):
    pass

def func3(m,n):
    pass

def func4(lst):
    pass
  
def func5(scoreDic,x):
    pass

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
    print(func6([39, 180, 123, 195, 156, 22, 91, 133, 26, 184]))  # [22, 91, 123, 133]
    print(func6([80, 84, 94, 188, 136, 68])) #[]
    print(func7("1a2b3.54x",(2, 4)))
    print(func7("1a2b3.54x",(7, 9)))
    print(func8("Claimed78"))  # True
    print(func8("remains"))  # False