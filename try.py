def qj_5(lst,center,K):
    if K==0:
        return False
    count=1
    for i in range(1,len(lst)):
        pre=lst[i-1]>center #用true和false判断是否在同一侧
        cur=lst[i]>center
        if pre==cur:
            count+=1
            if count>=K:
                return True
        else:
            count=1
    return False

def qj_2(str1,str2):
    num1=abs(ord(str1[0])-ord(str2[0]))
    num2=abs(int(str1[1])-int(str2[1]))
    if num1>num2:
        num1,num2=num2,num1
    step1=num1
    step2=num2-step1
    return step1+step2

def qj_3(lst):
    count=0
    score_plus=2
    if lst[0]==0:
        return 0
    elif lst[0]==1:
        score=2
    else:
        score=2
        count=1
    
    for i in lst[1:]:
        if i==0:
            break
        elif i==1:
            score+=1
            count=0
            score_plus=2
        else:
            if count==1:
                score_plus+=2
                score+=score_plus
            else:
                count=1
                score+=score_plus
                
    return score


print(qj_3([1,1,2,2,2,0,]))