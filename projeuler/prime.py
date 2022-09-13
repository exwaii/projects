from math import sqrt
from math import ceil
n = int(input("Check this number: "))
def isprime(x):
    for i in range(2,ceil(sqrt(x))):
        if x%i==0:
            print(i)
            return False
    return True
print(isprime(n))
