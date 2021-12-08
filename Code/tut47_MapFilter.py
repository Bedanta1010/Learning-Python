# Map, filter and reduce
# numbers = ["3", "35", "78", "45"]

# numbers = list(map(int, numbers))   # Map always returns an object
# print(map(int, numbers))   # Returns where the map object is

# numbers[2] = numbers[2] + 1
# print(numbers[2]), 

# num = [7, 9, 154, 74, 84, 3, 4, 7, 96]

# square = list(map(lambda x : x * x, num))
# print(square)


# def square(a):
#     return a * a


# def cube(a):
#     return a * a * a


# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x : x(i), func))
#     print(val)


# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def isGreater5(a):
#     return a > 5


# grThan5 = list(filter(isGreater5, list_1))
# print(grThan5)

# ======== Reduce ========

from functools import reduce

list1 = [7, 9, 1, 5, 6]
num = reduce(lambda x, y: x + y, list1)

print(num)
