grocery = ["Banana", "Processor", "Bhindi", "GPU", 56]
# print(grocery)
# print(grocery[1])

# numbers = [2, 7, 4, 17, 22]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

# Slicing is same as in tut8 file
# print(numbers[:3])  # While slicing the list is changed only for that statement and won't be applied globally but will .sort and .reverse the whole variable will be changed globally
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers.append(7)  # Will add the datatype at the end of list
# numbers.insert(1, 68)
# numbers.remove(7)
# numbers.pop()  # Will remove the last element
# numbers[1] = 98  # Will change the number in that index
# print(numbers)

# Mutable (can change) and Immutable (cannot change)
# tp = (1, 2, 3)
# tp = (1,)
# tp[1] = 98
# print(tp)
# In tp where there is parenthesis u can't change the values of it, i.e, it is immutable

a = 1
b = 8
a, b = b, a
print(a, b)
