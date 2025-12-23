def longest_cyclic_common_substring(s1, s2):
    # 展开字符环为两倍长度，模拟循环特性
    s1_expand = s1 + s1
    s2_expand = s2 + s2
    len1 = len(s1)
    len2 = len(s2)
    max_len = 0  # 记录最长公共子串长度

    # 遍历所有可能的子串长度（最大为两个字符串的最小长度）
    max_possible_len = min(len1, len2)
    res=''
    for l in range(1, max_possible_len + 1):
        # 遍历s1展开后的所有长度为l的子串（超过原长度则无需遍历）
        for i in range(len1):
            substr = s1_expand[i:i+l]
            # 检查该子串是否在s2的展开字符串中
            if substr in s2_expand:
                if l > max_len:
                    res=substr
    return res

# 计算并输出结果
print(longest_cyclic_common_substring('ABCDEFAGAGDEGKABUVKLM', 'MADJKLUVKL'))
print(longest_cyclic_common_substring('abc','def'))
