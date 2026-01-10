
n=int(input())
lst1=list(input())
k=int(input())
for i in lst1:
    if ' ' in lst1:
        lst1.remove(' ')
lst=[]
for i in lst1:
    lst.append(int(i))
lst2=list(set(lst))
lst2=sorted(lst2)
print(lst.count(lst2[k-1]))
