def L081_03(s):
    s_l=s.lower()
    words=s_l.split()
    lst=[]
    for word in words:
        pun=''
        if word[-1] in [',','.']:
            pun=word[-1]
            word=word[:-1]

        if word.endswith('ly'):
            word=word[:-2]+'lies'

        if word.endswith('ing') and len(word)>3:
            word = word[:-3]
        
        lst.append(word+pun)
    res=' '.join(lst)
    return res

if __name__ =="__main__":
    print(L081_03('Lilly is quicky swimming in a lake,two years later,bly set a world record.'))