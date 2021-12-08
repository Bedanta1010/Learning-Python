# Operator Overloading and Dunder Methods in Python
class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.noOfLeaves = newLeaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee ('{self.name}' , {self.salary} , '{self.role}')"

    def __str__(self):
        return f"{self.name} gets {self.salary} and role is {self.role}"


emp1 = Employee("Harry", 485, "Programmer")
emp2 = Employee("Rohan", 80, "Worker")

print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)  # Without __repr__ it will print object details (It always prefer __str__ first)
print(str(emp1))
print(repr(emp1))
print(repr(str(emp1)))

# Check docs for more Dunder Methods (Mapping Operators to Functions)
