def up(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfator=0.01
while up(dayfator)<37.78:
    dayfator+=0.01
print('工作日的努力参数是{:.3f}'.format(dayfator))