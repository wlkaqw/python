def func(tuple1):
    lst1=[]
    seq=[tuple1[0]]
    lst2=[]
    for i in tuple1[1:]:
        if i==seq[-1]+1:
            seq.append(i)
        else:
            lst1.append(tuple(seq))
            seq=[i]
    lst1.append(tuple(seq))
    max_=max(len(seq) for seq in lst1)
    lst2=[seq for seq in lst1 if len(seq)==max_]
    lst2.sort(key=lambda x:x[0],reverse=True)
    return lst2

print(func((1,3,5,7,9)))
