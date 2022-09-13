import math
from copy import copy
def isprime(number):
    a=int(math.sqrt(number))
    if number==1:
        return False
    elif number>=2:
        for i in range(2,a+1):
            if not number%i:
                return False
        else:
            return True


def iscircular(number):
    b=list(str(number))
    #if not ('2' in b or '5' in b or '0' in b):
    newlist=copy(b)
    for i in range(len(b)):
        newlist.insert(0,newlist.pop(-1))
        if not isprime(int("".join(newlist))):
            return False
        
print(iscircular(999331))
#print(isprime(999313))      
            
            
                
            
        
print(iscircular(13))        
primes=[]
aokay=[]
for i in range(1,1000001):
    if isprime(i):
        primes.append(i)
for i in range(len(primes)):
    if iscircular(primes[i]) is None:
        aokay.append(primes[i])
print(len(aokay))
