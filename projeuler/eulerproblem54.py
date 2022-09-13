f=open(r"C:\Users\xy\Documents\projeuler\p054_poker.txt","r")
hands=[]
for line in f:
    hands.append(list(map(list,line[:29].split(" "))))
wincount=0
ann=["T","J","Q","K","A"]
nann=[10,11,12,13,14]
def winner(handss):
    for i in range(0,10):
        if handss[i][0]in ann:
            handss[i][0]=nann[ann.index(handss[i][0])]
    handss=[int(handss[i][0]) for i in range(0,10)]
    check1={handss[i][0] for i in range(0,5)}
    check2={handss[i][0] for i in range(5,10)}
    if check1==set(nann):
        return True
    if check2==set(nann):
        return False
    check1=sorted(check1)
    check2=sorted(check2)
    if check1==[check1[0]+i for i in range(0,5)]:
        if check2==[=check2[0]+i for i in range(0,5)]:
            if check2[0]>check1[0]:
                return False
            else:
                return True
        return True
    if check2==[check2[0]+i for i in range(0,5)]:
        return False
    if len(check1)==2:
        if len(check2)!=2:
            return True
        
#for hand in hands:
    #if winner(hand):
        #wincount+=1



f.close()
