import re 
def func801(str1):
    pattern=r'^[1-9]\d{16}[0-9Xx]$'
    return bool(re.match(pattern,str1))

def func802(str1):
    pattern=r'\b-?\d+\b'
    return re.findall(pattern,str1)
    
def func803(phoneNum):
    pattern=r'^0\d{2}-\d{8}$|^0\d{3}-\d{7}$'
    return bool(re.match(pattern,phoneNum))

def func804(phoneNum):
    pattern1=r'^1\d{10}$'
    pattern2=r'^0\d{2}-\d{8}$|^0\d{3}-\d{7}$'
    if re.match(pattern1,phoneNum):
        return 1
    elif re.match(pattern2,phoneNum):
        return 2
    elif phoneNum in ['110','119','120']:
        return 3
    else:
        return 0
    
def func805(str1):
    pattern=r'([1-9]\d{3})-([0-2]{2})-([0-3]{2})'
    res=re.sub(pattern,r'\1年\2月\3日',str1)
    return res

if __name__=="__main__":
    print(func801("320527198808081679"))
    print(func802('hello 123 a45 67x 375'))
    print(func803("0512-1234567"))
    print(func804("1152-12345678"))
    print(func805("1949-10-1,中华人民共和国成立了"))