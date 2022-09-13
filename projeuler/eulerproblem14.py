#even n/2
#odd 3n+1

def process(number):
    n=1
    while number != 1:
        n+=1
        if not number % 2:
            number=number/2
        else:
            number=number*3+1
    return n
bigthingn=0
ns=[0,0]
#bigfatnub
for i in range(1,1000000):
    c=process(i)
    if c>ns[0]:
        ns[0]=c
        ns[1]=i
print(ns)

