i = 0
# while (True):
#     print(i)
#     if i == 45:
#         break
#     i = i + 1
# while (True):
#     if i + 1 < 5:
#         i = i + 1
#         continue
#     print(i + 1)
#     if i == 45:
#         break
#     i = i + 1

# Quiz
while True:
    i = int(input("Print your number: "))
    if i < 100:
        continue
    elif i >= 100:
        print("Congrats")
        break
    else:
        print("Error")
        break
