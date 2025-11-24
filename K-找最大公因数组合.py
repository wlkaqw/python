import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        return
    max_num = max(nums)

    # 统计每个数的出现次数
    cnt = [0] * (max_num + 1)
    for num in nums:
        cnt[num] += 1

    # 计算每个d的倍数出现的总次数
    prefix = [0] * (max_num + 1)
    for d in range(1, max_num + 1):
        for multiple in range(d, max_num + 1, d):
            prefix[d] += cnt[multiple]


    res = [0] * (n + 1)

    max_set_k = 0
    for d in range(max_num, 0, -1):
        total = prefix[d]
        if total == 0:
            continue
        start_k = max(max_set_k + 1, 1)
        end_k = min(total, n)
        if start_k > end_k:
            continue

        for k in range(end_k, start_k - 1, -1):
            res[k] = d
        max_set_k = end_k

        if max_set_k == n:
            break

    for i in range(1, n + 1):
        print(res[i])


if __name__ == "__main__":
    main()