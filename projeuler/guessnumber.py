from random import randint
print("welcome to the number guessing game!")
difficulty=input("easy or hard? e/h ")
number=randint(1,100)
EASYATTEMPTS=10
HARDATTEMPTS=6
if difficulty=="e":
    attempts=EASYATTEMPTS
else:
    attempts=HARDATTEMPTS
while attempts>0:
    print(f"you have {attempts} attempts left")
    attempts-=1
    guess=int(input("make a guess "))
    if guess==number:
        break
    if guess>number:
        print("too high ")
        print("guess again")
    else:
        print("too low")
        print("guess again")
if attempts==0:
    print("you lose, no more attempts ")
else:
    print("you guessed correctly!" )

    
