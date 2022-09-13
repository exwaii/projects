import math
a=list(str(math.factorial(100)))
a=list(map(int,a))
sum1=0
for i in range(len(a)):
    sum1+=a[i]
print(sum1)
