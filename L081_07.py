def L081_07(s):
    lst=[]
    s=s.swapcase()
    s=s[::-1]
    for char in s:
        if char.islower():
            new_=(ord(char)-ord('a')+3)%26+ord('a')
        else:
            new_=(ord(char)-ord('A')+3)%26+ord('A')
        lst.append(chr(new_))
    return ''.join(lst)

print(L081_07('abCD'))