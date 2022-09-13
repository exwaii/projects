import array as arr
import copy
import itertools
#listofnumbers=[0,1,2,3,4,5,6,7,8,9]
arrays=[]
for thingy in itertools.permutations("0123456789",10):
    #print(type(thingy))
    newthingy=list(thingy)
    for i in range(len(newthingy)):
        newthingy[i]=int(newthingy[i])
    temparr=arr.array("i",newthingy)
    arrays.append(temparr)
print(arrays[1000000-1])
