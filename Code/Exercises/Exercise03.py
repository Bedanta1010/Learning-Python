n = 85
guesses = 1
while guesses <= 9:
    num = int(input("Input the number you guessed: "))
    if num < n:
        print("The Guess is too small !")
        print("Number of Guesses Left", 9 - guesses)
        guesses = guesses + 1
        continue
    elif num > n:
        print("The Guess is too large !")
        print("Number of Guesses Left", 9 - guesses)
        guesses = guesses + 1
        continue
    else:
        print("Congrats you guessed the number in", guesses, "guesses !\n")
        print("You won !!")
        print("Number of Guesses Left", 9 - guesses)
        guesses = guesses + 1
        break

if guesses > 9:
    print("You Lose !!")
