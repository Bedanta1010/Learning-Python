print("Welcome to my Calculator")
num1 = float(input("Input your first Number: "))
num2 = float(input("Input your second Number: "))
symbol = input("Input the symbol which you want: ")
if symbol == "multiplication" or symbol == "*":
    print(num1 * num2)
elif symbol == "addition" or symbol == "+":
    print(num1 + num2)
elif symbol == "subtraction" or symbol == "-":
    print(num1 - num2)
elif symbol == "division" or symbol == "/":
    print(num1 / num2)
else:
    print("Please provide a correct input !")
