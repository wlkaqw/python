def func(s):
    lst=[chr(ord(s[i])+ord(s[i+1])) for i in range(len(s)-1)]
    lst.append(chr(ord(s[len(s)-1])+ord(s[0])))
    return ''.join(lst)

print(func('1234'))