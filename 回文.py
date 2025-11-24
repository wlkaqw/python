def huiwen(m,n):
    c=0
    if m>n:
        m,n=n,m
    for i in range(m,n+1):
        tn=i
        rn=0
        while tn>0:
            b=tn%10
            tn//=10
            rn=rn*10+b
        if rn==i:
            c+=1
    return c

print(huiwen(6718,40))
