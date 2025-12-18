from collections import Counter

def str_intersection_with_duplicates(s1, s2, keep_order=True):
    """
    求两个字符串的交集（保留重复字符，取最小出现次数）
    :param s1: 第一个字符串
    :param s2: 第二个字符串
    :param keep_order: 是否按s1的字符顺序返回（False则按字符排序）
    :return: 交集字符串
    """
    # 统计字符频率
    count1 = Counter(s1) #Counter('aabcc')＝Counter({'a':2,'c':2,'b':1})
    count2 = Counter(s2)
    
    # 取交集（每个字符保留小出现次数）
    inter_count = count1 & count2
    
    if not inter_count:
        return ""
    
    # 按s1的顺序拼接（保留重复）
    if keep_order:
        result = []
        temp_count = inter_count.copy()  # 临时计数，避免修改原Counter
        for char in s1:
            if temp_count.get(char, 0) > 0:
                result.append(char)
                temp_count[char] -= 1
        return ''.join(result)
    # 按字符排序后拼接
    else:
        return ''.join([char * cnt for char, cnt in sorted(inter_count.items())])

# 测试案例
if __name__ == "__main__":
    s1 = "aabccdde"
    s2 = "abbcceeff"
    # 按s1顺序的交集（a出现1次，b1次，c2次，e1次）
    print("按原顺序：", str_intersection_with_duplicates(s1, s2))  # abcce
    # 按字符排序的交集
    print("按排序：", str_intersection_with_duplicates(s1, s2, keep_order=False))  # abcce
