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








numbera=100
numberb=100
palindromes=[]
for i in range(numbera,1000):
    for j in range(numberb,1000):
        sum1=i*j
        if findpalindrome(sum1):
            palindromes.append(sum1)
bigpalindrome=palindromes[0]
for i in range(len(palindromes)):
    if palindromes[i]>bigpalindrome:
        bigpalindrome=palindromes[i]
print("thats a lot of palindromes")
#print(palindromes)
print(bigpalindrome)
