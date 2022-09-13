#refer to notebook
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
def prights(number):
    number1=number//2
    factors=findfactors(number1)
    rights=[]
    if len(factors)%2:
        b=len(factors)//2+1
    else:
        b=len(factors)//2
    for i in range(b):
        m=factors[i]
        n=number1//m-m
        if m>n>0 and coprime(m,n):
           if m%2==0 or n%2==0: 
                a=m**2-n**2
                b=m*n*2
                c=m**2+n**2
                if a**2+b**2==c**2 and a+b+c==number:
                    rights.append([a,b,c])
    return sorted(rights)
def findfactors(number):
    sortlist=set()
    a=int(math.sqrt(number))
    for i in range(1,a+1):
        if number%i==0:
            sortlist.add(i)
            sortlist.add(int(number/i))
    return sorted(list(sortlist))
def coprime(a,b):
    a=findfactors(a)
    b=findfactors(b)
    for i in range(1,len(a)):
        if a[i] in b:
            return False
    return True
def rights(number):
    result=[]
    owo=prights(number)
    factorss=findfactors(number)
    for i in range(len(owo)):
        result.append(owo[i])
    if isprime(number) is False:
        if len(factorss)%2:
            a=len(factorss)//2+1
        else:
            a=len(factorss)//2
        for i in range(a):
            uwu=prights(number//factorss[i])
            for j in range(len(uwu)):
                result.append(sorted([uwu[j][0]*factorss[i],uwu[j][1]*factorss[i],uwu[j][2]*factorss[i]]))
    return result
count=0
for i in range(2,1001):
    if len(rights(i))>count:
        count=len(rights(i))
        result=i
print(result)
