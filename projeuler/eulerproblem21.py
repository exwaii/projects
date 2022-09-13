import math
def divisorsum(number):
    sum1=0
    b=int(math.sqrt(number))
    for i in range(b):
        a=i+1
        c=number//a
        if number%a==0:
            sum1+=c+a
    sum1-=number
    return [number,sum1]
listofsums=[]
for i in range(1,10001):
    insertthing=divisorsum(i)
    listofsums.append(insertthing)
amics=[]
for i in range(len(listofsums)):
    for j in range(len(listofsums)):
        if listofsums[i][1]==listofsums[j][0] and listofsums[i][0]==listofsums[j][1] and listofsums[i][0]!=listofsums[j][0]:
            fititin=[]
            fititin.append(listofsums[i][0])
            fititin.append(listofsums[j][0])
            amics.append(fititin)
#print(listofsums)
print(amics)
sum1=0
refinedlist=[]
for i in range(len(amics)):
    sum1+=amics[i][0]
print(sum1)
