import time
import random

def is_prime_brute_force(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_miller_rabin(n, k=12):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    while True:
        c = random.randint(1, n - 1)
        f = lambda x: (pow(x, 2, n) + c) % n
        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d
    return n

def is_prime_pollards_rho(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = pollards_rho(n)
    return d == n

# 测试的20位素数
n = 10000000000000000393

# 暴力枚举法（因时间过长，实际仅理论分析，此处不执行）
# start_time = time.time()
# print(is_prime_brute_force(n))
# end_time = time.time()
# print("暴力枚举法运行时间:", end_time - start_time)

# 米勒-拉宾算法
start_time = time.time()
print("米勒-拉宾算法判定结果:", is_prime_miller_rabin(n))
end_time = time.time()
print("米勒-拉宾算法运行时间:", end_time - start_time)

# Pollard's Rho算法
import math
start_time = time.time()
print("Pollard's Rho算法判定结果:", is_prime_pollards_rho(n))
end_time = time.time()
print("Pollard's Rho算法运行时间:", end_time - start_time)
