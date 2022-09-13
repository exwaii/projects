sum1=0
onedigits=["one","two","three","four","five","six","seven","eight","nine"]
thetwos=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','ten']
twodigits=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety',]
threedigits=['onehundredand','twohundredand','threehundredand','fourhundredand','fivehundredand','sixhundredand','sevenhundredand','eighthundredand','ninehundredand']
def ones(number):
    if number==1:
        return (onedigits[0])
    if number == 2:
        return (onedigits[1])
    if number==3:
        return (onedigits[2])
    if number == 4:
        return (onedigits[3])
    if number==5:
        return (onedigits[4])
    if number == 6:
        return (onedigits[5])
    if number==7:
        return (onedigits[6])
    if number == 8:
        return (onedigits[7])
    if number==9:
        return (onedigits[8])
##    if number == 0:
##        return (onedigits[9])
def specialtwos(alist):
    if alist[1]==1:
        return (thetwos[0])
    if alist[1]==2:
        return (thetwos[1])
    if alist[1]==3:
        return (thetwos[2])
    if alist[1]==4:
        return (thetwos[3])
    if alist[1]==5:
        return (thetwos[4])
    if alist[1]==6:
        return (thetwos[5])
    if alist[1]==7:
        return (thetwos[6])
    if alist[1]==8:
        return (thetwos[7])
    if alist[1]==9:
        return (thetwos[8])
    if alist[1]==0:
        return (thetwos[9])
def twos(number):
    ##if number==1:
        #return (twodigits[0])
    if number == 2:
        return (twodigits[0])
    if number==3:
        return (twodigits[1])
    if number == 4:
        return (twodigits[2])
    if number==5:
        return (twodigits[3])
    if number == 6:
        return (twodigits[4])
    if number==7:
        return (twodigits[5])
    if number == 8:
        return (twodigits[6])
    if number==9:
        return (twodigits[7])
def threes(number):
    if number==1:
        return (threedigits[0])
    if number == 2:
        return (threedigits[1])
    if number==3:
        return (threedigits[2])
    if number == 4:
        return (threedigits[3])
    if number==5:
        return (threedigits[4])
    if number == 6:
        return (threedigits[5])
    if number==7:
        return (threedigits[6])
    if number == 8:
        return (threedigits[7])
    if number==9:
        return (threedigits[8])
for i in range(1,1001):
    z=list(str(i))
    for j in range(len(z)):
        z[j]=int(z[j])
    if len(z)==1:
        #sum1+=a
        print(ones(z[0]))
    elif len(z)==2:
        if z[0]==1:
            #b=
            print(specialtwos(z))
            #sum1+=b
        elif z[1]==0:
            print(twos(z[0]))
            #print(ones(z[1]))
            #sum1+=c+d
            #print(z)
        else:
            print(twos(z[0]))
            print(ones(z[1]))
    elif len(z)==3:
        if z[1]==1:
            x=[]
            x.append(z[1])
            x.append(z[2])
            #sum1+=e+f
            print(threes(z[0]))
            print(specialtwos(x))
        elif z[1]==0 and z[2]==0:
            #e=threes(z[0])
            #sum1+=e
            print(threes(z[0]))
        elif z[1]==0 and not z[2]==0:
            #f=threes(z[0])
            #g=ones(z[2])
            #sum1+=f+g
            print(threes(z[0]))
            print(ones(z[2]))
        elif not z[1]==0 and z[2]==0:
            #h=threes(z[0])
            #l=twos(z[1])
            #sum1+=h+l
            print(threes(z[0]))
            print(twos(z[1]))
        elif z[1]!=0 and z[2]!=0:
            m=threes(z[0])
            n=twos(z[1])
            o=ones(z[2])
            #sum1+=m+n+o
            print(threes(z[0]))
            print(twos(z[1]))
            print(ones(z[2]))
    elif len(z)==4:
        print("onethousand")
print(sum1)
        
            
        
