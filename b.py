
n=int(input()[0])
m=int(input()[1])
lst0=[([0]*n)*n]
for i in range(m):
    lst = list(map(int, input().split()))
    for a in range(n):
        for b in range(n):
            if lst[0] <= a <= lst[2] and lst[1] <= b <= lst[3]:
                lst0[a][b]+=lst[4]




