a=[["75"]
,["95 64"],
["17 47 82"],
["18 35 87 10"],
["20 04 82 47 65"],
["19 01 23 75 03 34"],
["88 02 77 73 07 63 67"],
["99 65 04 28 06 16 70 92"],
["41 41 26 56 83 40 80 70 33"],
["41 48 72 33 47 32 37 16 94 29"],
["53 71 44 65 25 43 91 52 97 51 14"],
["70 11 33 28 77 73 17 78 39 68 17 57"],
["91 71 52 38 17 14 91 43 58 50 27 29 48"],
["63 66 04 68 89 53 67 30 73 16 69 87 40 31"],
["04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]]
b=[]
for i in range(len(a)):
    ab=a[i][0].split()
    b.append(ab)
##    for j in range(len(a[i][0])):
##        a[i][j]=int(a[i][0][j])
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j]=int(b[i][j])
bigno=0
for i in range(len(b)):
    for j in range(len(b[i])):
        
##anewlist=[]
##for j in range(len(b[-2])):
##    if b[-1][j]>b[-1][j+1]:
##        anewlist.append(b[-1-1][j]+b[-1][j])
##    else:
##        anewlist.append(b[-1-1][j]+b[-1][j+1])
##print(anewlist)
##for i in range(len(b)-2):
####    print(b[-i-3])
##    for j in range(len(b[-i-3])):       
##        if j!=len(anewlist)-1:
##            if anewlist[j]>anewlist[j+1]:
##                anewlist[j]=anewlist[j]+b[-3][j]
##            else:
##                anewlist[j]=b[-1-1][j]+b[-1][j+1]
##        else:
##            if anewlist[j]>anewlist[j+1]:
##                anewlist[j]=anewlist[j]+b[-3][j]
##                anewlist.pop(j+1)
##            else:
##                anewlist[j]=b[-1-1][j]+b[-1][j+1]
##                anewlist.pop(j+1)
##print(anewlist)
