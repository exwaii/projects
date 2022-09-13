import math
triangles=[]
def ispentagon(number):
    number=number*24+1
    if (math.sqrt(number)).is_integer():
        if (math.sqrt(number))%6==5:
            return True
    return False
def ishexagonal(number):
    anew=math.sqrt(number*8+1)
    return ((anew+1)/4).is_integer()
a=286
while True:
    b=(a*(a+1))/2
    if ispentagon(b) and ishexagonal(b):
        print(b)
        break
    a+=1
