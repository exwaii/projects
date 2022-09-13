n=1
m=0
import math
while m<501:
    trianglenumber=0
    m=0
    factors=[]
    for i in range(1,n+1):
        trianglenumber+=i
    a=int(math.sqrt(trianglenumber))
    for i in range(1,a+1):
        if trianglenumber%i==0:
            factors.append(i)
            factors.append(trianglenumber//i)
    m=len(factors)
    n+=1
print(trianglenumber)
        
        
        
