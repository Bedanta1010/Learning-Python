# Static Methods in Python
class Employee:
    noOfLeaves = 8

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
karan = Employee.from_string("Karan-780-Coordinator")

# print(karan.salary)

print(karan.printgood('harry'))
print(Employee.printgood('test'))
