a=1
b=0
c=0
result=[1]
sum=0
while result[c]<4000000:
	n=a+b
	result.append(n)
	b=a
	a=n
	c=c+1
result.pop()
print(result)
newresult=[]
for i in range(len(result)):
        #print(i)
        newtest=i
        if result[i]%2==0:
                newresult.append(result[i])
print(newresult)
for i in range(len(newresult)):
        sum=sum+newresult[i]
print(sum)
