# Recursion and iteration

# def print2(str1):
#     print2(str1)
#     print("This is " + str1)


# print2("test")


def factorial_i(n):   # It was a iterative function
    """
    @param: n => Integer
    @return: n * n-1 * n-2 * n-3 * .....
    """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

    pass


def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)

    # 5 * 4 then
    # 5 * 4 * 3 then
    # 5 * 4 * 3 * 2...


# number = int(input("Enter a number: "))
# print("Iterative", factorial_i(number))
# print("Recursive", factorial_r(number))


# Quiz
def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


number = int(input("Enter a number: "))
print(fibonnaci(number))
