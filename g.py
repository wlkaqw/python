n=int(input())
s = list(map(int, input().split()))
count=0
for i in range(1,n-1):
    a=s[i+1]-s[i]
    if a<0:
        a+=4
    if a==0:
        count+=2
    elif a==1:
        count+=1
    elif a==2:
        count+=0
    else:
        count+=3
print(count)
