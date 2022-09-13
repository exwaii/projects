theset=set()
for i in range(2,101):
    for j in range(2,101):
        theset.add(i**j)

print(len(theset))
