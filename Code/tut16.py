# list1 = [["Harry", 2], ["Bedanta", 7], ["John", 9], ["Juman", 17]]
# for item in list1:
#     print(item)
# The below for loop thing will not work in dictionaries
# for item, lollipop in list1:
#     print(item, lollipop)

# dict1 = dict(list1)
# for item in dict1:
#     print(item)
# for item, lollipop in dict1.items():
#     print(item, "is", lollipop)

# Quiz
numList = [7, "Computer", 96, 78, 2, "Pen", 4, 55]
for item in numList:
    if str(item).isnumeric() and item > 6:
        print(item)
