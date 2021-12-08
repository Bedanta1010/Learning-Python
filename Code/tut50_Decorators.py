# Decorator in Python
# def funcret(num):
#     if num == 0:
#         return print
#
#     if num == 1:
#         return int
#
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
#
#
# executor(print)

# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#
#     return nowexec
#
#
# @dec1
# def who_is_harry():
#     print("Harry is a good boy")


# who_is_harry = dec1(who_is_harry)   # Instead of this put @dec1 above the def
# who_is_harry()
