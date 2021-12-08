# Scope, Global Variables and Global Keyword

l = 10  # Global Variable

# def func1(n):
#     l = 5  # Block Variable
#     m = 8

#     # l = l + 45   # It will throw if l is not present locally..

#     global b  # this will create a global variable b
#     b = 35

#     print(l, m)
#     print(n)


# func1("Test")
# print(b)
# print(l)


def harry():
    x = 20
    def rohan():
        global x
        x = 35  # Will still show 20 because it will find the global variable before harry func but if we add a x variable the harry function then it will work
    print("Before rohan function", x)
    rohan()
    print("After rohan function", x)

harry()
