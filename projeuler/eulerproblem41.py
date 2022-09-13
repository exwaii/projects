def ispandigital(number):
    length=len(str(number))
    if length==1:
        return False
    length=[str(i) for i in range(1,length+1)]
    a=list(str(number))
    for i in range(len(length)):
        if not length[i] in a:
            return False
    return True
import math
import time
start=time.time()
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
result=0
for i in range(7654321,0,-1):
    if isprime(i) and ispandigital(i):
        result=i
        break
print(result)
print('found in',time.time()-start,'seconds i wanna flex cause i never had one this fast')
