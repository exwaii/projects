def findcorners(n):
    squaredn=n**2
    a=n-1
    sum1=[]
    b=0
    for i in range(squaredn,1,-a):
        sum1.append(i)
        b+=1
        #print(i)
        if b==4:
            break
    return sum1
total=0
for i in range(3,1002,2):
    #print(i)
    a=findcorners(i)
    for i in range(len(a)):
        total+=a[i]
total+=1
print(total)
