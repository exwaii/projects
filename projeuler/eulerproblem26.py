primes=[]
import math
def f(d):
    x=1*9
    z=x
    k=1
    while z%d:
        z=z*10+x
        k+=1
    return [k,d]
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
for i in range(1,1001):
    if isprime(i):
        primes.append(i)
count=0
##print(f(2))
##for i in range(len(primes)):
##    print(1/primes[i])
for i in range(len(primes)):
    if not primes[i]==2:
        if not primes[i]==5:
            #print(primes[i])
            listed=f(primes[i])
            if listed[0]>count:
                count=listed[0]
                thefinalanswer=listed[1]
            #print(i)
print(thefinalanswer)
