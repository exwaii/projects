###jan 1900 1 is monday
###jan 1900 7 is sunday
###find out jan 1 1901
###jan 1 1901 was a friday
###next sunday?
###jan 1 1901
###jan 7 1900 is sun
###every 7 days from now is now sunday
###april june sept november is 30
###jan march may july oct dec is 31
###feb leap 29 norm 28
##
##def numberofsundays(number,number2):
##    count2=0
##    monthsindays=[31,28,31,30,31,30,31,31,30,31,30,31]
##    count=0
##    newlist=[]
##    newmonthindays=[]
##    if number%4==0:
##        monthsindays[1]=29
##    for i in range(len(monthsindays)):
##        #print(monthsindays[i])
##        count+=monthsindays[i]
##        newmonthindays.append(count)
##        #print(count)
##    #print(newmonthindays)
##    for i in range(number2,366,7):
##        if i in newmonthindays:
##            count2+=1
##        thefinalone=i
##    thefinalone=7+i-365
##    return [thefinalone,count2]
##def numberofsundayscentury(start1,date1,end1):
##    allsundays=0
##    a=numberofsundays(start1,date1)
##    for i in range(start1+1,end1+1):
##        a=numberofsundays(i,a[0])
##        allsundays+=a[1]
##    return allsundays
##print(numberofsundayscentury(1901,6,2000))
from datetime import date
sum1=0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).isoweekday()==7:
            sum1+=1
print(sum1)
