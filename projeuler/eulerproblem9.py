#a+b+c=1000
#a= m^2-n^2,b=2*m*n,c=m^2+n^2
#m^2-n^2+2*m*n*m^2+n^2=1000
#(m(n+m))/m^2+n*m=500
factorsof500=[]
for i in range(500):
    a=i+1
    if 500%a==0:
        factorsof500.append(a)
b=len(factorsof500)//2
for i in range(1,b):
    m=factorsof500[i]
    n=factorsof500[len(factorsof500)-i-1]-m
    a=m**2-n**2
    b=2*m*n
    c=m**2+n**2
    if a**2+b**2==c**2 and a+b+c==1000:
        print(a,b,c,a*b*c)
        
    

