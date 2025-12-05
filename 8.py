import re 
def func801(str1):
    pattern=r'^[1-9]\d{16}([-9Xx])$'
    return bool(re.match(pattern,str1))

def func802(str1):
    pattern=r'\b-?\d+\b'
    return re.findall(pattern,str1)
    
def func803(phoneNum):
    pass

def func804(phoneNum):
    pass

def func805(str1):
    pass
   

if __name__=="__main__":
    print(func802('hello 123 a45 67x 375'))