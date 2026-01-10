
'''n=int(input())'''
def func(m):
    str1 = str(m)
    if m != 33:
        for j in range(len(str1)):
            if str1[j:j + 2] == '33':
                str1 = str1[0:j] + str1[j + 2:]
                return int(str1)
    elif m>=33:
        m-=33
        return m
    else:
        return m
'''for i in range(n):
    s = int(input('ddd'))
    while s>0:
        s=func(s)
        if s==0:
            print('Yes')
            break
        elif s<33:
            print('No')
            break'''
print(func(165))
