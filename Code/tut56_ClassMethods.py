# Class Methods in Python
class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def changeLeaves(cls, newLeaves):   # cls is that class which is running in an instance of that object
        cls.noOfLeaves = newLeaves


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 255, "Student")

print(harry.noOfLeaves)
harry.changeLeaves(34)
print(harry.noOfLeaves)
