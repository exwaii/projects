import itertools
result=[]
primes=[2,3,5,7,11,13,17]
def divisible(numberlist):
    for j in range(1,8):
        a=numberlist[j:j+3]
        a=int("".join(a))
        if a%primes[j-1]:
            return False
    return True
        
for i in itertools.permutations('0123456789',10):
    test=list(i)
##    a=test[1:4]
##    a=int("".join(a))
    if test[0]!=0:
        if divisible(test):
            result.append(int(''.join(test)))
print(1406357289 in result)
    
print(sum(result),result)


