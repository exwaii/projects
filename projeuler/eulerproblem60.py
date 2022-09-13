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
primess=sieve(1000)
primess.pop(0)
b=[3,5,7,11,13]
check=None
for i in range(len(primess)):
    b[0]=primess[i]
    for j in range(i+1,len(primess)):
        b[1]=primess[j]
        itwo=True
        for same in list(permutations("01234",2)
                         ):
            if b[int(same[0])]==b[int(same[1])]:
                itwo=False
                mone=same
                break
        if itwo:
            for comby in list(permutations("01",2)):
                if not isprime(int("".join([str(b[int(comby[0])]),str(b[int(comby[1])])]))):
                    itwo=False
                    mone=comby
                    break
        print(b,itwo,mone)
        if not itwo:
            #print(b)
            continue
        for k in range(j+1,len(primess)):
            b[2]=primess[k]
            ithree=True
            for same1 in list(permutations("01234",2)):
                if b[int(same1[0])]==b[int(same1[1])]:
                    ithree=False
                    mtwo=same1
                    break
            if ithree:
                for comby1 in list(permutations("012",2)):
                    if not isprime(int("".join([str(b[int(comby1[0])]),str(b[int(comby1[1])])]))):
                        ithree=False
                        mtwo=comby1
                        break
            print(b,ithree,mtwo)
            if not ithree:
                #print(b)
                continue
            for l in range(k+1,len(primess)):
                ifour=True
                b[3]=primess[l]
                for same2 in list(permutations("01234",2)):
                    if b[int(same2[0])]==b[int(same2[1])]:
                        ifour=False
                        mthree=same2
                        break
                if ifour:        
                    for comby2 in list(permutations("0123",2)):
                        if not isprime(int("".join([str(b[int(comby2[0])]),str(b[int(comby2[1])])]))):
                            ifour=False
                            mthree=comby2
                            break
                print(b,ifour,mthree)
                if not ifour:
                    continue
                for m in range(l+1,len(primess)):
                    #print(b)
                    b[4]=primess[m]
                    #print(b)
                    check=True
                    for same3 in list(permutations("01234",2)):
                        if b[int(same3[0])]==b[int(same3[1])]:
                            check=False
                            mfour=same3
                            break
                    if check:
                        for comby3 in list(permutations("01234",2)):
                            #print(int("".join([str(b[int(comby[0])]),str(b[int(comby[1])])])))
                            if not isprime(int("".join([str(b[int(comby3[0])]),str(b[int(comby3[1])])]))):
                                check=False
                                mfour=comby3
                                break
                    print(b,check,mfour)
                    if not check:
                        continue
                    if check:
                        break
                if check:
                    break
            if check:
                break
        if check:
            break
    if check:
        break
##for i in range(len(primess)):
##    b[0]=primess[i]
##    for j in range(i+1,len(primess)):
##        b[1]=primess[j]
##        itwo=True
##        for comby in list(permutations("01",2)):
##            if not isprime(int("".join([str(b[int(comby[0])]),str(b[int(comby[1])])]))):
##                itwo=False
##                break
##        print(b,itwo)
##        if not itwo:
##            continue
##        for k in range(j+1,len(primess)):
##            b[2]=primess[k]
##            ithree=True
##            for comby1 in list(permutations("012",2)):
##                if not isprime(int("".join([str(b[int(comby1[0])]),str(b[int(comby1[1])])]))):
##                    ithree=False
##                    break
##            print(b,ithree)
##            if not ithree:
##                continue
##            for l in range(k+1,len(primess)):
##                ifour=True
##                b[3]=primess[l]
##                for comby2 in list(permutations("0123",2)):
##                    if not isprime(int("".join([str(b[int(comby2[0])]),str(b[int(comby2[1])])]))):
##                        ifour=False
##                        break
##                print(b,ifour)
##                if ifour:
##                    break
##                if not ifour:
##                    continue
##            if ifour:
##                break
##        if ifour:
####            break
##    if ifour:
##        break
##
##                                               
##                    
##
