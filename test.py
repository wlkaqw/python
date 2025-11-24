#例1
lst1=[2,3,9,15,16,34,27,33]
x=3

def panduan(lst,x):
    return sorted([num for num in lst if num%x==0])

#例2
lst2 = [lambda x:x**2 for i in range(5)]
print([lst2[i](i) for i in range(len(lst2))])
'''
第一个 i（lst2[i] 中的 i）：
表示列表 lst2 的索引，用于获取列表中第 i 个匿名函数（lambda 函数）。
第二个 i（(i) 中的 i）：
作为参数传递给获取到的 lambda 函数，即调用 lst2[i] 对应的函数时，传入的参数是 i。
简单说，就是用索引 i 取出列表中的第 i 个函数，再把 i 作为参数传给这个函数，最终计算的是 i 的平方
'''
