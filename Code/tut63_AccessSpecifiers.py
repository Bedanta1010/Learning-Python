# Public, Private & Protected Access Specifiers in Python
class Employee:
    noOfLeaves = 8  # Public
    _protected = 10   # Protected Variable
    __private = 98   # Private Variable

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.noOfLeaves = newLeaves

    @classmethod
    def from_string(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        return "This is good " + string


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 255, "Student")

print(harry._protected)

# print(harry.__private)   # This will throw a error
print(harry._Employee__private)   # This is called Name Mangling
