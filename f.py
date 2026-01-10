n = int(input())
for _ in range(n):
    s = input().strip()
    char_count = {}
    # 统计每个字符的出现次数
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    # 统计出现次数为奇数的字符数量
    odd_count = 0
    for cnt in char_count.values():
        if cnt % 2 != 0:
            odd_count += 1
    # 判断是否符合回文条件
    if (len(s) % 2 == 0 and odd_count == 0) or (len(s) % 2 == 1 and odd_count == 1):
        print("Yes")
    else:
        print("No")



