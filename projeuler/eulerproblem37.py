import math
def isprime(number1):
    a=int(math.sqrt(number1))
    if number1==1:
        return False
    elif number1>=2:
        for i in range(2,a+1):
            if not number1%i:
                #print(i)
                return False
        else:
            return True
    else:
        return False
def trunct(number):
##    newlist=list(str(number))
##    for j in range(0,len(str(number))):
##        if isprime(int("".join(newlist))):
##            newlist=[str(i) for i in newlist]
##            newlist=newlist[0:len(newlist)-1]
##            #print(newlist)
##        else:
##            return False
    
    while len(str(number))>1:
        if isprime(number):
            #print(number)
            flag=isprime(number)
            number=number//10
        else:
            flag=False
            break
    if isprime(number) is False:
        flag=False
    return flag
def detrunct(number2):
    while len(str(number2))>1:
        if isprime(number2):
            flag1=isprime(number2)
            number2=number2%(10**(len(str(number2))-1))
        else:
            flag1=False
            break
    if isprime(number2) is False:
        flag1=False
    return flag1
##primes=[True for i in range(0,73939134)]
##c=2
##prime2=[]
##while c**2<73939134:
##    if primes[c] is True:
##        for i in range(c*2,73939134,c):
##            primes[i]=False
##    c+=1
##for i in range(2,73939134):
##    if primes[i] is True:
##        prime2.append(i)
##print(prime2)
result=[]
for i in range(10,739398):    
    if trunct(i):
        #print(i)
        if detrunct(i):
            result.append(i)
print(sum(result),result,len(result))
    
