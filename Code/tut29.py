f = open("tut27j.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(0)  # It goes back to the specified index
print(f.tell())
print(f.readline())
# print(f.tell())

f.close()
