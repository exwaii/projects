a=[]
for i in range(1,1000000):
    a.append(str(i))
a="".join(a)
a=list(str(a))
newonesowo=[]
newonesowo.append(a[0])
newonesowo.append(a[9])
newonesowo.append(a[99])
newonesowo.append(a[999])
newonesowo.append(a[9999])
newonesowo.append(a[99999])
newonesowo.append(a[999999])
#newonesowo.append(a[9999999])
newonesowo=list(map(int,newonesowo))
sum=1
for i in range(len(newonesowo)):
    sum*=newonesowo[i]
print(sum)
