sum1=0
onedigits=["one","two","three","four","five","six","seven","eight","nine"]
thetwos=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','ten']
twodigits=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety',]
threedigits=['onehundredand','twohundredand','threehundredand','fourhundredand','fivehundredand','sixhundredand','sevenhundredand','eighthundredand','ninehundredand']
thethrees=['onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']

#def specialthrees(number):
def ones(number):
    if number==1:
        return len(onedigits[0])
    if number == 2:
        return len(onedigits[1])
    if number==3:
        return len(onedigits[2])
    if number == 4:
        return len(onedigits[3])
    if number==5:
        return len(onedigits[4])
    if number == 6:
        return len(onedigits[5])
    if number==7:
        return len(onedigits[6])
    if number == 8:
        return len(onedigits[7])
    if number==9:
        return len(onedigits[8])
##    if number == 0:
##        return len(onedigits[9])
def specialtwos(alist):
    if alist[1]==1:
        return len(thetwos[0])
    if alist[1]==2:
        return len(thetwos[1])
    if alist[1]==3:
        return len(thetwos[2])
    if alist[1]==4:
        return len(thetwos[3])
    if alist[1]==5:
        return len(thetwos[4])
    if alist[1]==6:
        return len(thetwos[5])
    if alist[1]==7:
        return len(thetwos[6])
    if alist[1]==8:
        return len(thetwos[7])
    if alist[1]==9:
        return len(thetwos[8])
    if alist[1]==0:
        return len(thetwos[9])
def twos(number):
    ##if number==1:
        #return len(twodigits[0])
    if number == 2:
        return len(twodigits[0])
    if number==3:
        return len(twodigits[1])
    if number == 4:
        return len(twodigits[2])
    if number==5:
        return len(twodigits[3])
    if number == 6:
        return len(twodigits[4])
    if number==7:
        return len(twodigits[5])
    if number == 8:
        return len(twodigits[6])
    if number==9:
        return len(twodigits[7])
def threes(number):
    if number==1:
        return len(threedigits[0])
    if number == 2:
        return len(threedigits[1])
    if number==3:
        return len(threedigits[2])
    if number == 4:
        return len(threedigits[3])
    if number==5:
        return len(threedigits[4])
    if number == 6:
        return len(threedigits[5])
    if number==7:
        return len(threedigits[6])
    if number == 8:
        return len(threedigits[7])
    if number==9:
        return len(threedigits[8])
def specialthrees(alist):
    if alist[0]==1:
        return len(thethrees[0])
    elif alist[0]==2:
        return len(thethrees[1])
    elif alist[0]==3:
        return len(thethrees[2])
    elif alist[0]==4:
        return len(thethrees[3])
    elif alist[0]==5:
        return len(thethrees[4])
    elif alist[0]==6:
        return len(thethrees[5])
    elif alist[0]==7:
        return len(thethrees[6])
    elif alist[0]==8:
        return len(thethrees[7])
    elif alist[0]==9:
        return len(thethrees[8])
##    if alist[1]==0:
##        return len(thethrees[9])
##threefourtwo=[342]
for i in range(1,1001):
    z=list(str(i))
    for j in range(len(z)):
        z[j]=int(z[j])
    if len(z)==1:
        a=ones(z[0])
        sum1+=a
##        print(z)
    elif len(z)==2:
        if z[0]==1:
            b=specialtwos(z)
##            print(z)
            sum1+=b
        elif z[1]==0:
            cd=twos(z[0])
            sum1+=cd
##            print(z)
        else:    
            c=twos(z[0])
            d=ones(z[1])
##            print(z)
            sum1+=c+d
    elif len(z)==3:
        if z[1]==1:
            e=threes(z[0])
            x=[]
            x.append(z[1])
            x.append(z[2])
            f=specialtwos(x)
            sum1+=e+f
            #print(z)
        elif z[1]==0 and z[2]==0:
            e=specialthrees(z)
            sum1+=e
            #print(z)
        elif z[1]==0 and not z[2]==0:
            f=threes(z[0])
            g=ones(z[2])
            sum1+=f+g
##            print(z)
        elif not z[1]==0 and z[2]==0:
            h=threes(z[0])
            l=twos(z[1])
            sum1+=h+l
##            print(z)
        elif z[1]!=0 and z[2]!=0:
            m=threes(z[0])
            n=twos(z[1])
            o=ones(z[2])
            sum1+=m+n+o
##            print(z)
    else:
        sum1+=len("onethousand")
print(sum1)
