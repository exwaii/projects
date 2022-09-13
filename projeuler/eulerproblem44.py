pentagons=[]
import math
for i in range(1,10000):
    pentagons.append((i*(i*3-1))//2)
print(pentagons)
def ispentagon(number):
    number=number*24+1
    if (math.sqrt(number)).is_integer():
        if (math.sqrt(number))%6==5:
            return True
    return False
check=False
for i in range(len(pentagons)):
    for j in range(i+1,len(pentagons)):
        if ispentagon(pentagons[j]-pentagons[i]) and ispentagon(pentagons[i]+pentagons[j]):
            print(pentagons[j]-pentagons[i])
            check=True
            break
    if check:
        break
