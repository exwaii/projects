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
for i in range(1,2000000):
    if isprime(i):
        primes.append(i)
sum=0
for i in range(len(primes)):
    sum+=primes[i]
print(sum)
