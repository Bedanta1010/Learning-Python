# __name__ == __main__ usage
def printh(string):
    return f"This is a string {string}"


def add(num1, num2):
    return num1 + num2 + 5


# The below will not be executed in the program where it is imported
# The value of __name__ here is main but in tut45_2.py it will be 'tut45_1'
if __name__ == '__main__':
    print(printh("Pizza"))
    o = add(4, 8)
    print(o)
