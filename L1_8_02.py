def func(tuple1):
    lst1=[]
    tuple2=[]
    for i in range(len(tuple1)-1):
        for j in range(i+1,len(tuple1)):
            seq=tuple1[i:j]
            if seq==tuple(reversed(seq)):
                lst1.append(seq)
    max_=max(len(seq) for seq in lst1)
    tuple2=(seq for seq in lst1 if len(seq)==max_)
    return tuple(lst2)

print(func((1,2,5,6,5,2,7,9)))