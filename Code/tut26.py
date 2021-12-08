# File IO Basics
"""
"r" = Open File for Reading - default
"w" = Open File for Writing
"x" = Creates File if doesn't exists
"a" = Add more content to a File
"t" = text mode - default
"b" = binary mode
"+" = read and write
"""

f = open("tut26i.txt")
# f = open("tut26i.txt", "rb")
# content = f.read()
# print(content)

# content = f.read(3)
# print(content)

# content = f.read(3)
# print(content)

# content = f.read(35478)
# print("1", content)

# content = f.read(3154)  # It wont print
# print("2", content)

# content = f.read()
# for line in content:
#     print(line)  # Will print character by character

# for line in f:
#     print(line, end="")  # Will print line by line

# print(f.readline())
# print(f.readline())

print(f.readlines())

f.close()  # Always close the files
