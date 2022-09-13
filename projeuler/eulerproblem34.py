import math
result=[]
for i in range(3,2540160):
    listed=list(str(i))
    count=0
    for j in range(len(listed)):
        count+=math.factorial(int(listed[j]))
    if count==i:
        result.append(i)
sum1=0
for i in range(len(result)):
    sum1+=result[i]
print(sum1)
