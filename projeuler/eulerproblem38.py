from itertools import count
def concatenate(number):
    concatenated=[]
    for i in count(1):
        concatenated.append(str(i*number))
        cocnumber="".join(concatenated)
        if len(cocnumber)>= 9:
            return int(cocnumber)
def ispandigital(number):
    length=len(str(number))
    if not length == 9:
        return False
    #length=[str(i) for i in range(1,length+1)]
    length=[str(i) for i in range(1,10)]
    a=list(str(number))
    for i in range(len(length)):
        if not length[i] in a:
            return False
    return True
print(ispandigital(123456789))
result=0
for i in range(2,1000000):
    no=concatenate(i)
    if ispandigital(no):
        if no>result:
            result=no
            count1=i
print(result,count1)
