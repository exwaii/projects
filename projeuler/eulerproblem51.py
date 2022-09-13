import math
import copy
from itertools import count
from itertools import permutations
from itertools import combinations
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
primess=sieve(1000000)
for i in range(len(primess)):
    check=False
    testprime = list(str(primess[i]))
    #"".join(testprimess)
    for k in range(len(testprime)-1):
        comby=list(combinations([x for x in range(len(testprime))],k+1))
        for l in range(len(comby)):
            testy=[i for i in testprime]
            smallcheck=False
            checking=testy[comby[l][0]]
            rip=False
            for o in range(1,len(comby[l])):
                if checking==testy[comby[1][o]]:
                    smallcheck=True
                else:
                    smallcheck=False
                if not smallcheck:
                    rip=True
                    break
                checking=testy[comby[1][o-1]]
            if rip:
                continue
            count=0
            check=False
            for n in range(1,10):
                for m in range(len(comby[l])):
                    testy[comby[l][m]]=str(n)
                if isprime(int("".join(testy))):
                    count+=1
                if count>8 and check==True:
                    check=False
                if count==8:
                    check=True
            if check:
                break
        if check==True:
            print(testprime)
            break
    if check:
        break
                    

                

                



    

    

