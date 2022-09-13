aset=set()
aset1=[]
from itertools import permutations

def check(number, first, second, aset, aset1):
    testin3="".join(list(number[(first+second):]))
    testin1="".join(list(number[0:first]))
    testin2="".join(list(number[first:(first+second)]))
    
    if int(testin1)*int(testin2)==int(testin3):
        aset.add(testin3)
        blist=[testin1,testin2,testin3]
        aset1.append(blist)


for number in permutations('123456789',9):
    #print(number)
    number=list(number)
##    testin2=[]
##    for ii in range(4,9):
##        testin2.append(number[ii])
##    testin2="".join(testin2)
##    testin21=[]
##    for ii in range(2):
##        testin21.append(number[ii])
##    testin22=[]
##    testin21="".join(testin21)
##    for ii in range(2,4):
##        testin22.append(number[ii])
##    testin22="".join(testin22)
##    if (testin21)*(testin22)==(testin2):
##        aset.add((testin2))
##        templist2=[(testin21),(testin22),(testin2)]
##        aset1.append(templist2)
####    testin3=[]
##    for ii in range(6,9):
##        testin3.append(number[ii])
##    testin3="".join(testin3)
##    testin31=[]
##    for ii in range(3):
##        testin31.append(number[ii])
##    testin32=[]
##    testin31="".join(testin31)
##    for ii in range(3,6):
##        testin32.append(number[ii])
##    testin32="".join(testin32)
##    if (testin31)*(testin32)==(testin3):
##        aset.add((testin3))
##        templist3=[(testin31),(testin32),(testin3)]
##        aset1.append(templist3)
##        pr(number)
##    testin2="".join([(number[5]),(number[6]),(number[7]),(number[8])])  
##    testin21="".join([(number[0]),(number[1])])
##    testin22=''.join([(number[2]),(number[3]),(number[4])])
##    if int(testin21)*int(testin22)==int(testin2):
##        aset.add(testin2)
##        blist=[testin21,testin22,testin2]
##        aset1.append(blist)
    
    check(number, 2, 3, aset, aset1)
    check(number, 3, 2, aset, aset1)
    check(number, 1, 4, aset, aset1)
    check(number, 4, 1, aset, aset1)
    
##    testin31="".join([(number[0]),(number[1]),(number[2])])
##    testin32=''.join([(number[3]),(number[4])])
##    if int(testin31)*int(testin32)==int(testin2):
##        aset.add(testin2)
##        blist=[testin31,testin32,testin2]
##        aset1.append(blist)
##        
##    testin1=number[0]
##    testin41="".join([number[1],number[2],number[3],number[4]])
##    #testin41="".join([number[1:5]])
##    if int(testin1)*int(testin41)==int(testin2):
##         aset.add(testin2)
##         blist=[testin1,testin41,testin2]
##         aset1.append(blist)
##    testin5=number[4]
##    testin51="".join([number[0],number[1],number[2],number[3]])
##    if int(testin5)*int(testin51)==int(testin2):
##        aset.add(testin2)
##        blist=[testin5,testin51,testin2]
##        aset1.append(blist)
print(aset,aset1)
thesum=0
for i in aset:
    thesum+=int(i)
print(thesum)
