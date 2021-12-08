# Super() and Overriding in Classes
class A:
    classvar1 = "I am a variable inside class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"   # This one is required in both the classes


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()   # If it is written below then the below code will be overwritten by the objects in class A
        self.classvar1 = "Instance var in Class B"
        self.var1 = "I am inside class B's constructor"
        # print(super().classvar1)  # To call a variable from class A


a = A()
b = B()

print(b.special)
print(b.classvar1)
print(b.var1)
