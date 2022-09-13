sortlist=[]
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

def findprime(number):
    prime=[]
    c=int(math.sqrt(number))
    for i in range(2,c+1):
        b=number%i
        a=number/i
        if b==0:
            #factors.append(i)
            if isprime(i) is True:
                prime.append(i)
            if isprime(a) is True:
                prime.append(a)
    return prime
print(findprime(600851475143))
#tiny bit more efficient lul          
        
#for i in range(len(factors)):
    #sortlist.append(factors[i])
#return factors

def numberoffactors(number):
    return len(findprime(number))
from itertools import count
count1=0
##for i in count(2):
##    if numberoffactors(i)==4:
##        print(i)
##        break
for i in count(210):
    if numberoffactors(i)==4 and count1==0:
        count1+=1
        #print(i)
    elif numberoffactors(i)==4 and count1>0:
        count1+=1
        #print(count1,i)
    elif numberoffactors(i)!=4 and count1>0:
        count1=0
    if count1==4:
        print(i-3,i-2,i-1,i)
        break
