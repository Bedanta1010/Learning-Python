import random

print("Welcome to snake, water and gun game !!")
print("Type s for Snake\nType w for Water\nType g for Gun")

attempts = 1
yPoint = 0
cPoint = 0

while attempts <= 10:
    lst = ["s", "w", "g"]
    compChoice = random.choice(lst)
    yourChoice = input("Input what you choose: ")
    yourChoice = yourChoice.lower()

    if yourChoice == compChoice:
        print("\nIt is a Tie !\n")

    elif yourChoice == "s" and compChoice == "w":
        yPoint = yPoint + 1
        print(f"\nYou chose snake and Computer chose water! ")
        print("The snake drank water\n")
        print("You won this round")
        print("You got 1 point\n")

    elif yourChoice == "w" and compChoice == "s":
        cPoint = cPoint + 1
        print(f"\nYou chose water and Computer chose snake! ")
        print("The snake drank water\n")
        print("You lost this round")
        print("Computer gets 1 point\n")

    elif yourChoice == "w" and compChoice == "g":
        print(f"\nYou chose water and Computer chose gun! ")
        yPoint = yPoint + 1
        print("The gun sank in water\n")
        print("You won this round")
        print("You got 1 point\n")

    elif yourChoice == "g" and compChoice == "w":
        print(f"\nYou chose gun and Computer chose water! ")
        cPoint = cPoint + 1
        print("The gun sank in water\n")
        print("You Lost this round")
        print("computer gets 1 point\n")

    elif yourChoice == "g" and compChoice == "s":
        print(f"\nYou chose gun and Computer chose snake! ")
        yPoint = yPoint + 1
        print("The snake was shot and it died\n")
        print("You won this round")
        print("You get 1 point\n")

    elif yourChoice == "s" and compChoice == "g":
        print(f"\nYou chose snake and Computer chose gun! ")
        cPoint = cPoint + 1
        print("The snake was shot and he died\n")
        print("You lost this round!")
        print("Computer gets 1 point\n")

    else:
        print("Invalid Input !")

    guesses = 10 - attempts
    print(f"No. of guesses left {guesses}")
    attempts = attempts + 1

    if attempts > 10:
        print("Game Over")

print(f"Your point is {yPoint} and Computer's point is {cPoint}")

if yPoint > cPoint:
    print("You Won !!")
elif yPoint < cPoint:
    print("You Lose !!")
else:
    print("It's a tie")
