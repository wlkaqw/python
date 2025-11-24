import math

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
    
def Try01(A,B):
    lst=[]
    lst1=[]
    for i in A:
        if is_prime(i):
            lst.append(i)
    for i in lst:
        if '3' in str(i) or '7' in str(i):
            lst1.append(i)

    points = []
    for i in range(0, len(lst1) - 1, 2):
        points.append( (lst1[i], lst1[i+1]) )

    m,n=B[0],B[1]
    max_=-1
    far=None
    for (x,y) in points:
        dist= ((m-x)**2+(n-y)**2)**0.5
        if dist>max_:
            max_=dist
            far=[x,y]
    return far

if __name__ == '__main__':
    print(Try01([2 ,68,4, 3, 5,7,90,11,13],[1,1]))
    print(Try01([2 ,68,4, 3, 5,7,90,11,13,17],[1,1]))
    print(Try01([37,2 ,68,4, 3, 5,7,90,11,13,17,19,23,29,31,37,400,37,37],[37,37]))
    print(Try01([37,2 ,68,4, 3, 5,7,90,11,13,17,19,23,29,31,37,400,37,37],[1,1]))
    print(Try01([2,68],[1,1]))
    print(Try01([2,5,68],[1,1]))
    print(Try01([2,5,7,68],[1,1]))
    print(Try01([2,3,7,68],[1,1]))
    print(Try01([2,3,3,7,68],[1,1]))