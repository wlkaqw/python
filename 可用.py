def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
def func1(num):
    if num <= 4:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and is_prime(i):
            j = num//i
            if is_prime(j):
                return True
    return False        

def no_is_prime(n):
    count=0
    num=2
    while True:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            count+=1
            if count==n:
                return num
        num+=1


