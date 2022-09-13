result=[]
a=1
b=0
c=0
testing=0
while testing<1000:
    n=a+b
    #print(n,a,b)
    result.append(n)
    b=a
    a=n
    testing=len(list(str(n)))
    c+=1
print(c+1)
