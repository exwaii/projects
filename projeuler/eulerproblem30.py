#a=2
result=[]
sum1=0
##while a<354294:
##    count=0
##    listeda=list(str(a))
##    for i in range(len(listeda)):
##        listeda[i]=int(listeda[i])
##        count+=listeda[i]**5
##    if count==a:
##        result.append(a)
for i in range(2,354294):
    listed=list(str(i))
    count=0
    for j in range(len(listed)):
        count+=int(listed[j])**5
    if count==i:
        result.append(i)
for i in range(len(result)):
    sum1+=result[i]
print(sum1)
