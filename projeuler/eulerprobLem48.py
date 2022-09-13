a=0
for i in range(1,1001):
   a+=i**i
print(a)
a=list(str(a))
print(int("".join([a[-i] for i in range(1,11)])))
