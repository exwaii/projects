from itertools import count
from time import sleep
a=1
b=0
count=1
print(count,a)
while True:
    sleep(0.1)
    c=b+a
    count+=1
    print(c/a)
    b=a
    a=c
    
