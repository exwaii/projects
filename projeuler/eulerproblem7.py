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
primes=[]
testing=1
while len(primes)<=10001: 
    if not testing==1:
        if testing==2:
            primes.append(testing)
        else:
            if isprime(testing):
                primes.append(testing)
    testing+=1
print(primes[10000])
