#====dictionary======
def func6201(lst):
    d={}
    for i in lst:
        key=i[:1]
        if key not in d:
            d[key]=[]
        d[key].append(i)
    return d

def func6202(lst):
    lst2=[]
    for i in lst:
        d={}
        lst1=[]
        lst1.extend(i[1:])
        lst1.remove(max(lst1))
        lst1.remove(min(lst1))
        ave=sum(lst1)/5
        d['name']=i[0]
        d['score']=ave
        lst2.append(d)
    return lst2

def func6203(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    d1=dict(sorted(d.items(),key=lambda x:x[0]))
    return d1

def func6204(dict1,dict2):
    lst1=[]
    lst2=[]
    lst1.extend(dict1.keys())
    lst2.extend(dict2.keys())
    return sorted(list(set(lst1)&set(lst2)))

def func6205(dict1,dict2):
    res=[]
    for i in dict1:
        for i in dict2:
            if dict1[i]==dict2[i]:
                res.append(i)
    return sorted(list(set(res)))


def func6206(lst1, lst2):
    d={}
    num=len(lst1)
    lst2=lst2[::-1]
    for i in range(num):
        d[lst1[i]+' '+lst2[i]]=i+18
    return d

def func6207(tp1, tp2):
    d={}
    num=len(tp1)
    for i in range(num):
        d[tp1[i]]=tp2[i]
    return d

def func6208(prices, quantities):
    num=0
    for i in prices:
        if i in quantities:
            num+=prices[i]*quantities[i]
    return num

def func6209(employee_dict):
    lst=[]
    for i in employee_dict:
        tp1=(i,employee_dict[i])
        lst.append(tp1)
    return sorted(lst, key=lambda x:x[1])

#=====set==========
def func6210(set1, set2):
    tp1=tuple(sorted(set1^set2))
    tp2=tuple(sorted(set1&set2,reverse=True))
    return tp1,tp2

def func6211(set1, set2):
    tp1 = tuple(sorted(set1 | set2))
    tp2 = tuple(sorted(set1 & set2, reverse=True))
    return tp1, tp2

if __name__=="__main__":
    print(func6211({1, 2, 3}, {3, 4, 5}))