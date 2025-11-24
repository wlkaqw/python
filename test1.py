import time
from sympy import factorint, isprime

def factor_large_odd(n):
    # 分解质因数
    factors = factorint(n)
    # 验证是否为两个素数的积
    if len(factors) != 2:
        return "输入数不是两个素数的积"
    p, q = list(factors.keys())
    # 验证是否为相近素数
    if max(p, q) / min(p, q) <= 2:  # 定义“相近”为倍数不超过2
        return p, q
    else:
        return "两个素数不相近"

# 测试样例（30位奇数，由两个相近素数相乘得到）
# 示例：p=123456789012345678901（15位素数），q=123456789012345678903（15位素数），n=p*q（30位）
p_test = 123456789012345678901
q_test = 123456789012345678903
n_test = p_test * q_test

# 运行并计时
start_time = time.time()
result = factor_large_odd(n_test)
end_time = time.time()

# 输出结果
print(f"测试样例n：{n_test}")
if isinstance(result, tuple):
    print(f"分解结果：{result[0]} × {result[1]}")
else:
    print(result)
print(f"运行时间：{end_time - start_time:.4f}秒")