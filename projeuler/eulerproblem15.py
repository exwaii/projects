import math
#(2,3) answer 10
def nCroute(gridnumber1,gridnumber2):
    nk=gridnumber1+gridnumber2
    top=math.factorial(nk)
    bottom=math.factorial(gridnumber1)*math.factorial(gridnumber2)
    possibilities=int(top/bottom)
    return possibilities
def ncr(numbe1,numbe2):
    top=math.factorial(numbe1)
    bottom=math.factorial(numbe2)*math.factorial(numbe1-numbe2)
    possibilities=int(top/bottom)
    return possibilities
print(ncr(4,2))
