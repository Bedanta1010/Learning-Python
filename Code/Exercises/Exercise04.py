n = int(input("Input the number of rows of stars you want: "))
m = int(input("Type 0 or 1: "))
new = bool(m)

if new:  # if new means if new == True
    for i in range(1, n + 1):  # range from 1'st index to n'th index
        for j in range(1, i + 1):  # it will start with a single * and with i number of *'s
            print("*", end="")  # The end func will add the number of stars behind
        print()  # Will create a new line after running the code
elif not new:
    for i in range(n, 0, - 1):  # range will go on reverse order because of 3rd parameter
        for j in range(1, i + 1):
            print("*", end="")  # Similar to the above end func
        print()  # Will create a new line after running the code
