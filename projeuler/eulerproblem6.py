squareofsum=0
squareofnumbers=0
for i in range(1,101):
    squareofnumbers+=i**2
print(squareofnumbers)
for i in range(1,101):
    squareofsum+=i
squareofsum=squareofsum**2
print(squareofsum)
print(squareofsum-squareofnumbers)
