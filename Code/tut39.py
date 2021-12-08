# F-String and String Formation
import math

me = "Rohan"
a1 = 3

# a = "My name is %s %s" % (me, a1)
# print(a)

# a = "This is {} {}"
# b = a.format(me, a1)
# print(b)

# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)

a = f"This is {me} {a1} {math.cos(60)}"
print(a)

# learn about time module
