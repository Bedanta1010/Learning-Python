mystr = "rohan is a good boy"
# print(mystr[4])
# print(mystr[0:5])  # It will print till the 4th index
# print(len(mystr))
# print(mystr[0:78])   # Will remove the warn and will print till which index it is available but if we use print(mystr[78]) then it will show error
# print(mystr[0:5:2])  # Will print 0, 2, 4th indexes
# print((mystr[0::2]))  # If there is nothing after the colon then it will take the last index and before the colon then it will take the first index
# print(mystr[-4:-2])  # Negative indexes means the indexes from behind
# print(mystr[::-1])  # Will print the string in negative order

print(mystr.isalnum())  # al num is alpha-numeric
print(mystr.endswith('boy'))  # End index
print(mystr.count('o'))
print(mystr.capitalize())
print(mystr.find('is'))  # Will show the index where the str is started
print(mystr.lower())
print(mystr.upper())
print(mystr.replace('is', 'are'))
