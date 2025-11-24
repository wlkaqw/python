temptrans=input('输入温度')
if temptrans[-1] in ['F','f']:
    c=(eval(temptrans[0:-1])-32)/1.8
    print('转换后的温度是{:.2f}c'.format(c))
elif temptrans[-1] in ['C','c']:
    f=1.8* eval(temptrans[0:-1])+32
    print('转换后的温度是{:.2f}f'.format(f))
else:
    print('格式错误')
