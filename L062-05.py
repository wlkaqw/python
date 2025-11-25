def factor_count(n):
    """计算正整数n的因子数量"""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # 若i是平方根，只加1；否则加2
            count += 1 if i * i == n else 2
            return count
def classify_by_factor(tup):
    # 步骤1：按因子数量分类
    factor_dict = {}
    for num in tup:
        cnt = factor_count(num)
        if cnt not in factor_dict:
            factor_dict[cnt] = []
        factor_dict[cnt].append(num)
                                                                                                                        
    # 步骤2：对每个列表升序排序
    for cnt in factor_dict:
        factor_dict[cnt].sort()
    
    # 步骤3：按因子数量降序排列，转换为元组序列
    sorted_items = sorted(factor_dict.items(), key=lambda x: -x[0])
    return tuple(sorted_items)