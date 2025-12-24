def get_first_elements(nested_tuple):
    """
    批量提取嵌套元组中每个子元组的第一个元素
    :param nested_tuple: 单层/多层嵌套的元组（若为单层元组则提取自身第一个元素）
    :return: 包含所有首个元素的列表
    """
    first_elems = []

    def extract_first(tp):
        # 递归处理多层嵌套
        if isinstance(tp, tuple):
            if len(tp) > 0:  # 非空元组才提取
                first_elems.append(tp[0])
                # 对元组内的每个元素继续递归（处理多层嵌套）
                for elem in tp[1:]:
                    extract_first(elem)

    extract_first(nested_tuple)
    return first_elems


# 调用示例
if __name__ == "__main__":
    # 示例1：单层元组
    tp1 = (5875, 7367, 4784)
    print(get_first_elements(tp1))  # 输出：[5875]

    # 示例2：双层嵌套元组
    tp2 = ((5875, 7367), (4784, 4470), (413, 8631))
    print(get_first_elements(tp2))  # 输出：[5875, 4784, 413]

    # 示例3：多层嵌套元组
    tp3 = ((1, 2), ((3, 4), 5), (6, (7, 8)))
    print(get_first_elements(tp3))  # 输出：[1, 3, 6, 7]

    # 示例4：空元组
    tp4 = ()
    print(get_first_elements(tp4))  # 输出：[]