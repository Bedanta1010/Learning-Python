# f = open("tut30.txt")
# print(f.readline())
#
# f.close()

with open("tut30.txt") as f:
    a = f.read(4)
    print(a)
