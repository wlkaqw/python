def shai(list1,list2,list3):
    total2=list(set(list1)&set(list2))
    total3=list(set(list1)&set(list2)&set(list3))
    return[total2,total3]

def shai1(lst):
    temp=[]
    for i in lst:
        i=set(i)
        temp.extend(i)
    st=set(temp)
    dt={}
    for i in st:
        dt[i]=temp.count(i)
    l2=sorted([k for k,v in dt.items() if v==2])
    l3=sorted([k for k,v in dt.items() if v==3])
    return[l2,l3]


if __name__ =="__main__":
    print(shai())