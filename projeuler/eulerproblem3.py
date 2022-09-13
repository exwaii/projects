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
def factors(number):
    sortlist=[]
    a=int(math.sqrt(number))
    for i in range(1,a+1):
        if number%i==0:
            sortlist.append([i,number/i])
    return sorted(sortlist)
def findfactors(number):
    sortlist=[]
    a=int(math.sqrt(number))
    for i in range(1,a+1):
        if number%i==0:
            sortlist.append(i)
            sortlist.append(number/i)
    return sorted(sortlist)
#ineffficient lul
def findprimefactors(number):
    sortlist=[]
    a=int(math.sqrt(number))+1
    for i in range(1,a+1):
        if number%i==0:
            if isprime(i):
                sortlist.append(i)
            if isprime(number/i):
                sortlist.append(number//i)
    return sorted(sortlist)
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
    return prime
print(findprime(12))
#returns [prime,power] in a list
