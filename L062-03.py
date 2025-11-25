def L062_03(lst):
    for i in range(len(lst)-1,-1,-1):
        for j in range(len(lst)):
            if i==j:
                continue
            else:
                if is_dominated(lst[j],lst[i]):
                    lst.pop(i)
                    break
    lst.sort(key=lambda x:x[0])
    return lst
def is_dominated(tup1,tup2):
    flag=False
    for i in range(len(tup1)):
        if tup1[i]>tup2[i]:
            break
        elif tup1[i]<tup2[i]:
            flag=True
    else:
        return flag
    return False

def process_list(L):
         # 筛选不被任何元组支配的元组
    result = []
    for t in L:
        # 假设当前元组不被支配
        is_not_dominated = True
        for other in L:
            if t == other:
                continue  # 跳过自身
                # 判断other是否支配t
            if (other[0] <= t[0] and other[1] <= t[1]) and (other[0] < t[0] or other[1] < t[1]):
                is_not_dominated = False
                break
        if is_not_dominated:
            result.append(t)
    # 按元组第一个元素从小到大排序
    result.sort(key=lambda x: x[0])
    return result
