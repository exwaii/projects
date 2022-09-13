result=[]
sortlist=[]
sum=0
for i in range(1,1000):
    sortlist.append(i)
#print(sort)
for i in range(len(sortlist)):
    if sortlist[i]%3 == 0:
        result.append(sortlist[i])
    elif sortlist[i]%5 == 0:
        result.append(sortlist[i])
for i in range(len(result)):
    sum=result[i]+sum
print(sum)
