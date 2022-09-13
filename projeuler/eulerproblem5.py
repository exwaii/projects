from copy import copy
import math
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
def findprimefactors(number):
    sortlist=[]
    a=int(math.sqrt(number))+1
    for i in range(1,a+1):
        if number%i==0:
            if isprime(i):
                sortlist.append(i)
            if isprime(number/i):
                sortlist.append(number//i)
    return sortlist
def findprime(number):
    if number==1:
        return [[1,1]]
    prime=[]
    number1=copy(number)
    a=list(set(findprimefactors(number)))
    for i in range(len(a)):
        number1=number1//a[i]
        count=1
        while number1%a[i]==0:
            number1=number1//a[i]
            count+=1
        prime.append([a[i],count])
    return sorted(prime)
def lcm(list1):
    list1=sorted(list1)
    primes=[]
    powers=[]
    for i in range(len(list1)):
        a=findprime(list1[i])
        for j in range(len(a)):
            if a[j][0] not in primes:
                primes.append(a[j][0])
                powers.append(a[j][1])
            if a[j][0] in primes:             
                if a[j][1]>powers[primes.index(a[j][0])]:
                    powers[primes.index(a[j][0])]=a[j][1]
    result=1
    for i in range(len(primes)):
        result*=primes[i]**powers[i]
    return result
def hcf(list1):
    list1=sorted(list1)
    primes=[]
    powers=[]
    for i in range(len(list1)):
        a=findprime(list1[i])
        for j in range(len(a)):
            if a[j][0] not in primes:
                primes.append(a[j][0])
                powers.append(a[j][1])
            if a[j][0] in primes:             
                if a[j][1]<powers[primes.index(a[j][0])]:
                    powers[primes.index(a[j][0])]=a[j][1]
    result=1
    for i in range(len(primes)):
        result*=primes[i]**powers[i]
    return result
print(lcm([i for i in range(1,100)]))
