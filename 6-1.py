from platform import mac_ver


def func6101(weights):
    lst=[]
    for i in range(len(weights)):
        lst.append(weights[i])
    ave=sum(lst)/len(lst)
    var=0
    for i in lst:
        var+=(i-ave)**2
    var/=len(lst)
    return "{:.3f}".format(var)

def func6102(elements):
    lst=[]
    for i in elements:
        if i in lst:
            pass
        else:
            lst.append(i)
    return lst

def func6103(numbers):
    num=len(numbers)
    max_=max(numbers)
    min_=min(numbers)
    average=sum(numbers)/num
    return tuple([num,max_,min_,average])

def func6104(numbers):
    return tuple(sorted(list(set(numbers))))


if __name__=="__main__":
    print(func6104((96, 722, 895, 257, 257, 97, 162, 239, 37, 838, 865, 25, 549, 779, 159, 447, 877, 1, 68, 234)))