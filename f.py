n=int(input())
for i in range(n):
    s = list(map(int, input().split()))
    count = 0
    for j in s:
        if s.count(j)==2:
            pass
        if s.count(j)==1:
            count+=1
    if count>1:
        print('No')
    else:
        print('Yes')




