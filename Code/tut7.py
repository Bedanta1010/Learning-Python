var1 = "Hello World"
var2 = 4
var3 = 36.7
# print(var1)
# print(type(var1))
# print(var2 + var3)
# print(var1 + var2) #This Will be an error because you cant add string with numbers
var4 = "32"
var5 = "48"
# print(var1 + var4)
# Typecasting
# print(int(var4) + var3)
# Other types of typecasting commands are str() [string], float() [float]

# print(10 * "Hello World\n")
# print(10 * str(int(var4) + int(var5)))  # This will override the sum getting multiplied by 10

# Quiz to make calculator for two numbers
print("Type the two number you want to calculate")
print("Enter your first number")
firstNum = input()
print("Enter your second number")
secondNum = input()
print("Answer is", float(firstNum) + float(secondNum))
