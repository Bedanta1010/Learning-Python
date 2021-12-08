num1 = input("Number 1: ")
num2 = input("Number 2: ")
try:
    print("Sum is", int(num1) + int(num2))
except Exception as err:
    print(err)

print("This line is imp")
