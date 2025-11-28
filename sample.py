def func6101(weights):
    ave=sum(weights)/len(weights)
    var=0
    for i in weights:
        var+=(i-ave)**2
    var/=ave
    return f"{var:.3f}"

def func6102(elements):
    lst=[]
    for i in elements:
        if i in lst:
            continue
    else:
        lst.append(i)
    return lst

def func6103(numbers):
    num=len(numbers)
    max_=max(numbers)
    min_=min(numbers)
    ave=sum(numbers)/num
    return (num,max_,min_,ave)

def func6104(numbers):
    return tuple(sorted(list(set(numbers))))



if __name__=="__main__":
    print(func6104((96, 722, 895, 257, 257, 97, 162, 239, 37, 838, 865, 25, 549, 779, 159, 447, 877, 1, 68, 234)))