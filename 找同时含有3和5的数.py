c=0 #用来计数
for i in range(1,1001):
    tn=i
    a = 0
    b = 0
    while tn !=0:
        d=tn%10
        tn//=10
        if d==3:
            a=1
        elif d==5:
            b=1
        if a==1 and b==1:
            c+=1
            print("{0:>5d}".format(i),end=" ")
            if c%5==0:
                print("")
            tn=0