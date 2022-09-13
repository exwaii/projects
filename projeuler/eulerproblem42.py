f=open("words.txt","r")
if f.mode=="r":
    contents=f.read()
contents=contents.split('","')
contents[0]='A'
contents[-1]='YOUTH'
triangles=[]
for i in range(1,101):
    triangles.append(i*(i+1)//2)
result=0
for i in range(len(contents)):
    testing=list(str(contents[i]))
    temp=0
    for j in range(len(testing)):
        temp+=ord(testing[j])-64
    if temp in triangles:
        result+=1
print(result)
