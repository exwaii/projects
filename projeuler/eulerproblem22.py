f=open("names.txt","r")
if f.mode=="r":
    contents=f.read()
#contents=list(contents)
contents=contents.split('","')
contents[0]="MARY"
contents[-1]="ALONSO"
#use a tuple? list but unchangeable
#tuples are comparable
import array as arr
arrays=[]
for i in range(len(contents)):
    a=list(str(contents[i]))
    for j in range(len(a)):
        a[j]=ord(a[j])-64
    b=arr.array("i",a)
    arrays.append(b)   
newordlist=sorted(arrays)
print(newordlist)
newchrlist=[]
bigsum=0
for i in range(len(newordlist)):
    sum1=0
    for j in range(len(newordlist[i])):
        sum1+=newordlist[i][j]
    #print(sum1)
    abc=sum1*(i+1)
    bigsum+=abc
print(bigsum)
##for i in range(len(newordlist)):
##    chrlist=[]
##    for j in range(len(newordlist[i])):
##        a=chr(newordlist[i][j])
##        chrlist.append(a)
##    newchrlist.append(chrlist)
##print(newchrlist)
##print(type(newchrlist[1]))
