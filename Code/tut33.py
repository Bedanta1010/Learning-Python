# Anonymouse or Lambda Functions
# Lambda is one line function while def is multiple lines. Lambda is also known as Anonymous function

minus = lambda x, y: x - y

print(minus(81, 45))


def a_first(a):
    return a[1]


a = [[1, 14], [7, 2], [9, 17], [8, 12]]
a.sort(key=a_first)
print(a)
