def func01(type,mode):
    if type not in [0,1] or mode not in [0,1,2]:
        return -1
    price=0
    if mode==0:
        price+=40
        if type==1:
            price+=5 
    elif mode==1:
        price+=58
        if type==1:
            price+=10
    else:
        price+=138
        if type==1:
            price+=20
    return price

def func02(lst):
    count=0
    for i in lst:
        score=i[0]*.2+i[1]*.8
        if score>=60:
            count+=1
    return "{0:.2f}".format(count/len(lst))

def func03(n):
    count=0
    num=2
    while True:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            count+=1
            if count==n:
                return num
        num+=1

def func04(lst,n1,n2):
    if n1<0 or n2<0 or n1>=n2:
        return lst
    if n2>=len(lst):
        n2=len(lst)-1
    lst1=lst[n1:n2+1]
    lst1.sort(reverse=True)
    lst=lst[:n1]+lst1+lst[n2+1:]
    return lst

def func05(m,n,number):
    dict={}
    for i in range(m,n+1):
        dict[i]=str(i).count(str(number))
    lst=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    return lst

def func06(lst):
    dict={}
    set1=set(lst)
    for i in set1:
        dict[i]=str(lst).count(str(i))
        lst1=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    if len(lst)>3:
        return [x[0] for x in lst1][0:3]
    return [x[0] for x in lst1]

def func08(string,ext):
    dict={}
    lst1=string.split(' ')
    lst15=[]
    lst2=[]
    while ' ' in lst1:
        lst1.remove(' ')
    for i in lst1:
        if i.endswith(ext):
            lst15.append(i)
    for i in lst15:
        if i.lower()[:-len(ext)-1] ==i.lower()[:-len(ext)-1][::-1]:
            lst2.append(i)
    for i in lst2: 
        dict[i]=len(i)
    lst3=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    return lst3[0][0]
  

print(func08("aba.txt aBa.doc    a..a.txt abba.ttxt", "docx"))
<<<<<<< HEAD
=======























>>>>>>> 01c363d475d910f09c2fd6bc4f1872fb1c943b51
        