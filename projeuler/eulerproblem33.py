listoflists=[]
for i in range(10,100):
    listed1=list(str(i)) #digits of numerator
    for j in range(10,100): 
        listed2=list(str(j)) #digits of denominator
        if i/j < 1:
            if not listed1[1] == "0" and not listed2[1] == "0": #if aoth digits are 0
                a=i/j
                for k in range(len(listed1)):
                    listed1[k]=int(listed1[k])
                for l in range(len(listed2)):
                    listed2[l]=int(listed2[l])
##                if listed1[0]/listed2[0]==a or listed1[1]/listed2[0]==a or listed1[1]/listed2[1]==a or listed1[0]/listed2[1]==a:
##                    a=[i,j]
##                    listoflists.append(a)
                if listed1[0]/listed2[0]==a:
                    if listed1[1]==listed2[1]:
                        aa=[i,j]
                        listoflists.append(aa)
                elif listed1[1]/listed2[0]==a:
                    if listed1[0]==listed2[1]:
                        aa=[i,j]
                        listoflists.append(aa)
                elif listed1[1]/listed2[1]==a:
                    if listed1[0]==listed2[0]:
                        aa=[i,j]
                        listoflists.append(aa)
                elif listed1[0]/listed2[1]==a:
                    if listed1[1]==listed2[0]:
                        aa=[i,j]
                        listoflists.append(aa)
print(listoflists)

from fractions import Fraction        
#print(Fraction(0.010000000000000002))
###for i in range(len(listoflists)):
    #print(listoflists[i])
    #print(Fraction(listoflists[i]))

    
