def findpalindrome(number):
    number=int(number)
    choppedup=list(str(number))
    #print(choppedup)
    reversedlist=[]
    for i in range(len(choppedup)):
        reversedlist.append(choppedup[len(choppedup)-i-1])
        #print(choppedup[len(choppedup)-i-1])
    for i in range(len(reversedlist)):
        reversedlist[i]=str(reversedlist[i])
    #print(reversedlist)
    "1".join(reversedlist)
    #print(reversedlist)
    listnumber=list(str(number))
    #print(reversedlist , strnumber)
    if reversedlist==listnumber:
        return True
    else:
        return False
result=[]
print(findpalindrome(123456787654321))
def binaryform(number):
   thenumber=[]
   def binary(number,thenumber):
      if number>=1:
         #print(number)
         b=number%2
         thenumber.insert(0,b)
         number=number//2
         binary(number,thenumber)
   binary(number,thenumber)
   thenumber = [str(i) for i in thenumber]
   thenumber=int("".join(thenumber))
   return thenumber
for i in range(1,1000001):
   if findpalindrome(i):
      if findpalindrome(binaryform(i)):
         result.append(i)

print(sum(result))
result2=[]
#alternatively, faster
for i in range(1,1000001):
   if findpalindrome(i):
      if findpalindrome(bin(i)[2:]):
         result2.append(i)
print(sum(result2))
