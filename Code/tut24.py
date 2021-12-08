a = 19
b = 17
c = sum((a, b))  # built in function


# print(c)


# def func1(a, b):
#     print("You are in function 1", a + b)
#
#
# def func2(a, b):
#     average = (a + b) / 2
#     print(average)
#
#
# func1(7, 9)
# func2(7, 9)


# print(func1())  # Throws None (since there is no return func in the function block) unlike while using only func1()

# def func3(a, b):
#     average = (a + b) / 2
#     # print(average)
#     return average
#
#
# v = func3(15, 89)
# print(v)


def func4(a, b):
    """This is a func that will calc the average"""
    average = (a + b) / 2
    # print(average)
    return average


print(func4.__doc__)
