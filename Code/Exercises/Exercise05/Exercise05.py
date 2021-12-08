import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        n = int(input("Input 1 for exercise and 2 for food: "))
        if n == 1:
            val = input("Input the exercise you just did: ")
            with open(".\Exercise05\harry-ex.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
        elif n == 2:
            val = input("Input what you ate: ")
            with open(".\Exercise05\harry-fd.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
    elif k == 2:
        n = int(input("Input 1 for exercise and 1 for food: "))
        if n == 1:
            val = input("Input the exercise you just did: ")
            with open(".\Exercise05\rohan-ex.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
        elif n == 2:
            val = input("Input what you ate: ")
            with open(".\Exercise05\rohan-fd.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
    elif k == 3:
        n = int(input("Input 1 for exercise and 1 for food: "))
        if n == 1:
            val = input("Input the exercise you just did: ")
            with open(".\Exercise05\hammad-ex.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
        elif n == 2:
            val = input("Input what you ate: ")
            with open(".\Exercise05\hammad-fd.txt", "w") as f:
                f.write(str([str(gettime())]) + ":" + val + "\n")
            print("File was updated !")
    else:
        print("Input 1 for harry, 2 for rohan and 3 for hammad")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open(".\Exercise05\harry-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif c == 2:
            with open(".\Exercise05\harry-fd.txt") as f:
                for i in f:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open(".\Exercise05\rohan-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif c == 2:
            with open(".\Exercise05\rohan-fd.txt") as f:
                for i in f:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open(".\Exercise05\hammad-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif c == 2:
            with open(".\Exercise05\hammad-fd.txt") as f:
                for i in f:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("Health Management System")
a = int(input("press 1 to lock the value and 2 for retrieve "))

if a == 1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)
