def func701(s):
    if len(s)<2:
        return ''
    return s[0:2]+s[-2:]

def func702(s, n):
     return s[:n - 1] + s[n:]

def func703(s):
    str1=s.split()
    str2=str1[::-1]
    return ' '.join(str2)

def func704(password):
    if len(password) < 8:
        return False
    has_digit = False
    has_lower = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
    return has_digit and has_lower and has_upper

def func705(s):
    processed = []
    for char in s:
        if char in (' ', '.', ',', '!'):
            continue
        processed.append(char.lower())
    return processed == processed[::-1]

def func706(s):
    encrypted = []
    for char in s:
        # 处理字母（忽略大小写）
        if char.isalpha():
            # 转为小写后计算对应的两位数字（a→01, b→02...z→26）
            num = ord(char.lower()) - ord('a') + 1
            encrypted.append("{:02d}".format(num))  # 格式化补零为两位
        # 处理数字
        elif char.isdigit():
            # 数字1→a, 2→b...9→i
            letter = chr(ord('a') + int(char) - 1)
            encrypted.append(letter)
    # 拼接所有加密后的字符
    return ''.join(encrypted)


if __name__=="__main__":
    print(func706("abc123"))