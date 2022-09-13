import math
abundants=set()
def abundantornot(number):
    sum1=0
    b=int(math.sqrt(number))
    for i in range(b):
        a=i+1
        c=number//a
        if number%a==0 and c!=a:
            sum1+=c+a
        elif number%a==0 and c==a:
            sum1+=a
    sum1-=number
    if sum1>number:
        abundants.add(number)
for i in range(1,20161+1):
    abundantornot(i)
print(len(abundants))
totalsum=set()
check=False
for i in range(1,20161+1):
    for j in abundants:
        if i-j in abundants:
            totalsum.add(i)
            break
    if check:
        break
##    if count==1:
##        count=1
##    elif count==0:
        
print(sum(range(1,20161+1))-sum(totalsum))
