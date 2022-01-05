import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
while chances<5:
    Guess=int(input("Guess Between 1 to 9= "))
    if (Guess==number):
        print("Congratulations You Won")
    elif(Guess<number):
        print("Your Guess Is Too Low, Enter A Higher Number")
    else:
        print("Your Guess Is Too High , Enter A Lower Number")
    chances+=1

if not chances <5:
    print("You Loose!! The number is ",number)