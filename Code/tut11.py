s = set()
# print(type(s))
# s_from_list = set([1, 2, 3, 4])
# print(s_from_list)

s.add(1)  # Set only adds unique values, if u use duplicate then it will not put inside the set
s.add(2)
# s.remove(2)
# s1 = s.union({1, 2, 3})
# s1 = s.intersection({1, 2, 3})
# print(s, s1)
s1 = {4, 7, 8}
print(s.isdisjoint(s1))
