def reverse_bits(x):
    if x == 0:
        return 0
    # 转换为二进制字符串（去掉前缀 '0b'）
    binary = bin(x)[2:]
    # 翻转二进制字符串
    reversed_binary = binary[::-1]
    # 转换回十进制
    return int(reversed_binary, 2)

n, m = map(int, input().split())
a = list(map(int, input().split()))
diff = [reverse_bits(num) - num for num in a]

# dp[i][j] 表示前i个元素中选j个不相交区间的最大和
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 不选第i个元素
        dp[i][j] = dp[i - 1][j]
        # 选第i个元素，寻找以i结尾的最优区间
        max_val = 0
        current = 0
        for k in range(i, 0, -1):
            current += diff[k - 1]
            if current > max_val:
                max_val = current
            if max_val + dp[k - 1][j - 1] > dp[i][j]:
                dp[i][j] = max_val + dp[k - 1][j - 1]

print(sum(a) + dp[n][m])
