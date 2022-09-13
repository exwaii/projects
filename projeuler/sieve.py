import math
import copy
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
def sieve(limit):
    primes=[True for i in range(1,limit+1)]
    sievelist=[i for i in range(1,limit+1)]
    for i in range(1,int(math.sqrt(limit))):
        if primes[i] is True:
            for j in range(i+i+1,limit,i+1):
                #print(j)
                primes[j]=False
    primes1=[]
    primes[0]=False
    for i in range(limit):
        if primes[i] is True:
            primes1.append(sievelist[i])
    return primes1
print(sieve(1000))
    



            

